#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'requests',
    'pandas>=1.1',
    'lxml>4.6',
]

setup_requirements = []

test_requirements = []

setup(
    author="Peter Andorfer",
    author_email='peter.andorfer@oeaw.ac.at',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="Utility functions to interact with geonames.org",
    entry_points={
        'console_scripts': [
            'acdh_geonames_utils=acdh_geonames_utils.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    package_data={
        '': ['fixtures/*.*'],
    },
    keywords='acdh_geonames_utils',
    name='acdh_geonames_utils',
    packages=find_packages(include=[
        'acdh_geonames_utils',
        'acdh_geonames_utils.*']
    ),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/acdh-oeaw/acdh_geonames_utils',
    version='0.5.0',
    zip_safe=False,
)
