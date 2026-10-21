# acdh_geonames_utils

[![codecov](https://codecov.io/gh/acdh-oeaw/acdh-geonames-utils/graph/badge.svg?token=w38AlUjm8X)](https://codecov.io/gh/acdh-oeaw/acdh-geonames-utils)
[![Test](https://github.com/acdh-oeaw/acdh-geonames-utils/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-geonames-utils/actions/workflows/test.yml)
[![Lint](https://github.com/acdh-oeaw/acdh-geonames-utils/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-geonames-utils/actions/workflows/lint.yml)
[![PyPI version](https://badge.fury.io/py/acdh-geonames-utils.svg?icon=si%3Apython)](https://badge.fury.io/py/acdh-geonames-utils)

Utility functions to interact with geonames.org

## Features

To use Geonames Utils in a project

```python
from acdh_geonames_utils import acdh_geonames_utils as gn

geonames_df = gn.dwonload_to_df('AT')
geonames_df.head() # prints the first n rows
```
