==============
Geonames Utils
==============


.. image:: https://img.shields.io/pypi/v/acdh_geonames_utils.svg
        :target: https://pypi.python.org/pypi/acdh_geonames_utils

.. image:: https://img.shields.io/travis/acdh-oeaw/acdh_geonames_utils.svg
        :target: https://travis-ci.com/acdh-oeaw/acdh_geonames_utils

.. image:: https://codecov.io/gh/acdh-oeaw/acdh_geonames_utils/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/acdh-oeaw/acdh_geonames_utils

.. image:: https://readthedocs.org/projects/geonames-utils/badge/?version=latest
        :target: https://geonames-utils.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Utility functions to interact with geonames.org


* Free software: MIT license
* Documentation: https://geonames-utils.readthedocs.io/


Features
--------

To use Geonames Utils in a project::

    from acdh_geonames_utils import acdh_geonames_utils as gn

    geonames_df = gn.dwonload_to_df('AT')
    geonames_df.head() # prints the first n rows

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
