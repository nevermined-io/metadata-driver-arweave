#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "nevermined-metadata-driver-interface>=0.2.0",
    "arweave-python-client~=1.0.14",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest",
]

setup(
    author="nevermined-io",
    author_email="root@nevermined.io",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    description="🐳 Metadata Arweave Driver (Python).",
    extras_require={"test": test_requirements, "dev": test_requirements},
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="nevermined-metadata-driver-arweave",
    name="nevermined-metadata-driver-arweave",
    packages=find_packages(include=["metadata_driver_arweave"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/nevermined-io/metadata-driver-arweave",
    version="0.1.3",
    zip_safe=False,
)
