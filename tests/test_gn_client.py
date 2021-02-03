#!/usr/bin/env python

"""Tests for `acdh_geonames_utils.gn_client` module."""

import unittest
from acdh_geonames_utils import gn_client

RDF_URL = "https://sws.geonames.org/2772400/about.rdf"
GN_ID = "2772400"


class Test_utils(unittest.TestCase):
    """Tests for `acdh_geonames_utils.utils` module."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.gn_obj = gn_client.gn_as_object(RDF_URL)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_parse_url(self):
        doc = gn_client.fetch_rdf(RDF_URL)
        self.assertEqual(f"{type(doc)}", "<class 'lxml.etree._Element'>")

    def test_002_doc_as_object(self):
        self.assertEqual(GN_ID, self.gn_obj['geonameid'])
        self.assertEqual(self.gn_obj['name'], 'Linz')
        self.assertEqual(self.gn_obj['country code'], 'AT')
        self.assertEqual(self.gn_obj['longitude'], 14.28611)
        self.assertEqual(
            f"{type(self.gn_obj['alternatenames'])}",
            "<class 'list'>"
        )

    def test_003_dl_rdfxml(self):
        dl = gn_client.dl_rdfxml(RDF_URL)
        self.assertEqual(dl, f"gn_rdf__{GN_ID}.xml")
