# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


if __name__ == '__main__':
    from ast import literal_eval
    from configparser import RawConfigParser
    from pathlib import Path
    from setuptools import setup, find_packages

    config = RawConfigParser()
    ROOT = Path(__file__).parent
    config.read_string('[version]\n' + (ROOT / 'dazl' / '_version.py').read_text())

    dazl_version = literal_eval(config.get('version', '__version__'))

    with open('README.md', 'r') as f:
        long_description = f.read()

    setup(
        name='dazl',
        version=dazl_version,
        packages=find_packages(include=['dazl', 'dazl.*'],
                               exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
        python_requires='>=3.6',
        url='https://digitalasset.com',
        author='Digital Asset (Switzerland) GmbH',
        author_email='support@digitalasset.com',
        description='high-level Ledger API client for DAML ledgers',
        long_description=long_description,
        long_description_content_type="text/markdown",
        entry_points={'console_scripts': ['dazl=dazl.cli:main']},
        keywords='dazl daml blockchain dlt distribute ledger digital asset da',
        include_package_data=True,
        install_requires=[
            'dataclasses;python_version<"3.7"',
            'grpcio>=1.20.1',
            'protobuf>=3.7.1',
            'PyYAML',
            'semver',
            'toposort',
        ],
        extras_require={
            'prometheus_client': ['prometheus_client'],
            'pygments': ['pygments'],
        },
        classifiers=[
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ])
