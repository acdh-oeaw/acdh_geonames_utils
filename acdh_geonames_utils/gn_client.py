import lxml.etree as ET
import requests

from acdh_geonames_utils.utils import sanitize_rdf_url, extract_id

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
    """retrieves the rdf/xml of the given geonames url/id and returns an lxml.etree
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


def dl_rdfxml(gn_id):
    """downloads the rdf/xml of the given geonames url/id and returns the file-name
    :param url: A GND-URL or ID,
    e.g. https://www.geonames.org/2772400/linz.html, 2772400
    :type url: str
    :return: the filename, something like gn_rdf__{gn_id}.xml
    :rtype: str
    """
    file_name = f"gn_rdf__{extract_id(gn_id)}.xml"
    doc = fetch_rdf(gn_id)
    with open(file_name, 'wb') as f:
        f.write(ET.tostring(doc, encoding="UTF-8"))
    return file_name


def gn_as_object(gn_id):

    doc = fetch_rdf(gn_id)
    gn_obj = {}
    gn_obj['geonameid'] = extract_id(
            doc.xpath(
                ".//rdfs:isDefinedBy/@rdf:resource",
                namespaces=NS_MAP
            )[0]
        )
    gn_obj['name'] = doc.xpath(
        ".//gn:name",
        namespaces=NS_MAP
    )[0].text
    gn_obj['asciiname'] = doc.xpath(
        ".//gn:name",
        namespaces=NS_MAP
    )[0].text
    gn_obj['alternatenames'] = doc.xpath(
        ".//gn:alternateName/text()",
        namespaces=NS_MAP
    )
    gn_obj['asciiname'] = doc.xpath(
        ".//gn:name",
        namespaces=NS_MAP
    )[0].text
    gn_obj['latitude'] = float(doc.xpath(
        ".//wgs84_pos:lat",
        namespaces=NS_MAP
    )[0].text)
    gn_obj['longitude'] = float(doc.xpath(
        ".//wgs84_pos:long",
        namespaces=NS_MAP
    )[0].text)
    gn_obj['country code'] = doc.xpath(
        ".//gn:countryCode",
        namespaces=NS_MAP
    )[0].text
    gn_obj['feature class'] = doc.xpath(
        ".//gn:featureClass/@rdf:resource",
        namespaces=NS_MAP
    )[0].split('#')[1]
    gn_obj['feature code'] = doc.xpath(
        ".//gn:featureCode/@rdf:resource",
        namespaces=NS_MAP
    )[0].split('#')[1]
    return gn_obj
