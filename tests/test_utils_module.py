#!/usr/bin/env python

"""Tests for `acdh_geonames_utils.utils` module."""

import unittest

import acdh_geonames_utils.utils as gn_utils

GOOD_IDS = [
    "https://sws.geonames.org/2772400/about.rdf",
    "https://www.geonames.org/2772400/linz.html",
    "2772400"
]
GOOD_ID = "2772400"
RDF_URL = "https://sws.geonames.org/2772400/about.rdf"


class Test_utils(unittest.TestCase):
    """Tests for `acdh_geonames_utils.utils` module."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_extract_id(self):
        for x in GOOD_IDS:
            self.assertEqual(gn_utils.extract_id(x), GOOD_ID)

    def test_002_sanitize_rdf_url(self):
        for x in GOOD_IDS:
            self.assertEqual(gn_utils.sanitize_rdf_url(x), RDF_URL)
