import lxml.etree as ET
import requests

from acdh_geonames_utils.utils import sanitize_rdf_url


def fetch_rdf(gn_id):
    """downloads the rdf/xml of the given geonames url/id and returns an lxml.etree
    :param url: A GND-URL or ID, e.g. https://www.geonames.org/2772400/linz.html, 2772400
    :type url: str
    :return: the rdf/xml as `lxml.etree._Element`
    :rtype: 'lxml.etree._Element'
    """
    gn_rdf_uri = sanitize_rdf_url(gn_id)
    res = requests.get(gn_rdf_uri)
    doc = ET.fromstring(res.content)
    return doc
