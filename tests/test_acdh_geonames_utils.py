#!/usr/bin/env python

"""Tests for `acdh_geonames_utils` package."""

import os
import unittest
from click.testing import CliRunner

from acdh_geonames_utils import acdh_geonames_utils as gn
from acdh_geonames_utils import cli

good_country_code = 'YU'
bad_country_code = 'BAAAD'

TEST_GN_FILE = os.path.join(
    "./fixtures",
    "AL.txt"
)


class TestAcdh_geonames_utils(unittest.TestCase):
    """Tests for `acdh_geonames_utils` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_download(self):
        """Test download of zip."""
        good = gn.download_country_zip(good_country_code)
        bad = gn.download_country_zip(bad_country_code)
        self.assertTrue(good.endswith(f"{good_country_code}.zip"))
        self.assertEqual(bad, "")

    def test_002_download_and_unzip(self):
        """Test download and unzip."""
        good = gn.download_and_unzip_country_zip(good_country_code)
        bad = gn.download_and_unzip_country_zip(bad_country_code)
        self.assertTrue(good.endswith(f"{good_country_code}.txt"))
        self.assertEqual(bad, "")

    def test_003_unzip(self):
        """Test unzipping of zip."""
        bad = gn.unzip_country_zip("")
        self.assertEqual(bad, "")

    def test_004_file_to_df(self):
        """Test loading file into pandas.DataFrame"""
        df = gn.countries_as_df(TEST_GN_FILE)
        self.assertEqual(len(df), 9356)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'acdh_geonames_utils.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
