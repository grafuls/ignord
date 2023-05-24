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
.. |docs| image:: https://readthedocs.org/projects/ignord/badge/?style=flat
    :target: https://ignord.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/grafuls/ignord/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/grafuls/ignord/actions

.. |codecov| image:: https://codecov.io/gh/grafuls/ignord/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/grafuls/ignord

.. |version| image:: https://img.shields.io/pypi/v/ignord.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ignord

.. |wheel| image:: https://img.shields.io/pypi/wheel/ignord.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ignord

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ignord.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ignord

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ignord.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ignord



.. end-badges

`ignord` is a Python CLI application that generates git ignore files for a specific language.

* Free software: GNU Lesser General Public License v3 (LGPLv3)

Installation
============

::

    pip install ignord

You can also install the in-development version with::

    pip install https://github.com/grafuls/ignord/archive/main.zip


Documentation
=============


https://ignord.readthedocs.io/


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
