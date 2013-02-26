#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import os

setup(
    name = "django-versionfield",
    version = "0.1",
    url = 'https://github.com/mindsnacks/django-versionfield',
    license = 'BSD',
    description = "A DB Independent Custom Django Field for storing Version numbers for fast indexing",
    author = 'Tom Hoddes',
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)