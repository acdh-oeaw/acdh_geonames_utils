#!/usr/bin/env python

"""Tests for `acdh_geonames_utils.gn_client` module."""

import unittest
from acdh_geonames_utils import gn_client

RDF_URL = "https://sws.geonames.org/2772400/about.rdf"


class Test_utils(unittest.TestCase):
    """Tests for `acdh_geonames_utils.utils` module."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.gn_obj = gn_client.doc_as_object(RDF_URL)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_parse_url(self):
        doc = gn_client.fetch_rdf(RDF_URL)
        self.assertEqual(f"{type(doc)}", "<class 'lxml.etree._Element'>")

    def test_002_doc_as_object(self):
        self.assertEqual(RDF_URL, self.gn_obj['geonameid'])
        self.assertEqual(self.gn_obj['name'], 'Linz')
        self.assertEqual(
            f"{type(self.gn_obj['alternatenames'])}",
            "<class 'list'>"
        )
