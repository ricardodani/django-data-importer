#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="django-data-importer",
    version="0.0.2",
    description="",
    author="Felipe 'chronos' Prenholato",
    author_email="philipe.rp@gmail.com",
    url="http://github.com/chronossc/django-data-importer",
    packages = find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    install_requires=[
        "Django >= 1.2.7",
        "openpyxl",
        "xlrd"
    ],
    zip_safe = False,
)
