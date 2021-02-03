import lxml.etree as ET
import requests

from acdh_geonames_utils.utils import sanitize_rdf_url

NS_MAP = {
    "gn": "http://www.geonames.org/ontology#",
    "cc": "http://creativecommons.org/ns#",
    "dcterms": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "wgs84_pos": "http://www.w3.org/2003/01/geo/wgs84_pos#"
}


def fetch_rdf(gn_id):
    """downloads the rdf/xml of the given geonames url/id and returns an lxml.etree
    :param url: A GND-URL or ID,
    e.g. https://www.geonames.org/2772400/linz.html, 2772400
    :type url: str
    :return: the rdf/xml as `lxml.etree._Element`
    :rtype: 'lxml.etree._Element'
    """
    gn_rdf_uri = sanitize_rdf_url(gn_id)
    res = requests.get(gn_rdf_uri)
    doc = ET.fromstring(res.content)
    return doc


def doc_as_object(gn_id):
    doc = fetch_rdf(gn_id)
    gn_obj = {}
    gn_obj['geonameid'] = doc.xpath(
        ".//rdfs:isDefinedBy/@rdf:resource",
        namespaces=NS_MAP
    )[0]
    gn_obj['name'] = doc.xpath(
        ".//gn:name",
        namespaces=NS_MAP
    )[0].text
    gn_obj['alternatenames'] = doc.xpath(
        ".//gn:alternateName/text()",
        namespaces=NS_MAP
    )
    return gn_obj