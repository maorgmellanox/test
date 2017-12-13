#!/usr/bin/env python
"""
setup.py file for SWIG python_verbs
"""
import sys
from setuptools import setup, find_packages


if sys.version_info < (2, 6):
    sys.exit('requires python 2.6 and up')

setup(
    name='test',
    version='0.1',
    packages=find_packages("src"),
)
