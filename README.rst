========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-ignor/badge/?style=flat
    :target: https://python-ignor.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/grafuls/python-ignor/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/grafuls/python-ignor/actions

.. |codecov| image:: https://codecov.io/gh/grafuls/python-ignor/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/grafuls/python-ignor

.. |version| image:: https://img.shields.io/pypi/v/ignor.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ignor

.. |wheel| image:: https://img.shields.io/pypi/wheel/ignor.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ignor

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ignor.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ignor

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ignor.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ignor

.. |commits-since| image:: https://img.shields.io/github/commits-since/grafuls/python-ignor/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/grafuls/python-ignor/compare/v0.0.0...main



.. end-badges

ignor is a Python CLI application that generates git ignore files for a specific language.

* Free software: GNU Lesser General Public License v3 (LGPLv3)

Installation
============

::

    pip install ignor

You can also install the in-development version with::

    pip install https://github.com/grafuls/python-ignor/archive/main.zip


Documentation
=============


https://python-ignor.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
