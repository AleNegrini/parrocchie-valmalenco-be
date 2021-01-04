# -*- coding: utf-8 -*-
"""
    Setup file for parrocchie_valmalenco_be.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import VersionConflict, require
import setuptools

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":

    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="parrocchie_valmalenco_be",
        version="0.0.1",
        author="Alessandro Negrini",
        author_email="alessandro.negrini@gmail.com",
        description="Backend code for Parrocchie Valmalenco",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/AleNegrini/parrocchie-valmalenco-be",
        packages=['parrocchie_valmalenco_be'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6'
    )
