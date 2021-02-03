import re
from acdh_geonames_utils.config import GN_RDF_TMPL


def extract_id(url):
    """extracts the geonames id from an geonames-URL
    :param url: A GND-URL, e.g. https://www.geonames.org/2772400/linz.html
    :type url: str
    :return: The geonames id, e.g. 2772400
    :rtype: str
    """
    gn_id = "".join(re.findall("[0-9]", url))
    return gn_id


def sanitize_rdf_url(url):
    """returns the url to the entitiy rdf-endpoint
    :param url: A GND-URL or id, e.g.
    https://www.geonames.org/2772400/linz.html, 27772400
    :type url: str
    :return: The geonames rdf-url, "https://sws.geonames.org/2772400/about.rdf"
    :rtype: str
    """
    gn_id = extract_id(url)
    return GN_RDF_TMPL.format(gn_id)
