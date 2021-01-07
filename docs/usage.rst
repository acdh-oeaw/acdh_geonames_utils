=====
Usage
=====

To use Geonames Utils in a project::

    from acdh_geonames_utils import acdh_geonames_utils as gn

    geonames_df = gn.download_to_df('AT')
    geonames_df.head() # prints the first n rows
