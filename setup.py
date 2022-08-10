#!/usr/bin/env python
from setuptools import setup
from pytest_rmsis import __prog__, __version__, __author__, __email__, __description__, __keywords__, __license__, __url__
setup(
    name=__prog__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license=__license__,
    url=__url__,
    keywords=__keywords__,
    classifiers=[
        'Framework :: Pytest',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=["pytest_rmsis"],
    install_requires=[
        'pytest>=5.3.5',
        'sgqlc>=12.1'
    ],
    entry_points={
        'pytest11': [
            'pytest_rmsis = pytest_rmsis.plugin',
        ]
    },
)
