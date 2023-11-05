#!/usr/bin/env python
"""The setup script."""
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

name = 'jane_doe.dev_test'
author = 'Jane Doe'
author_email = 'jande.doe@null.com'
description = 'Marcom CG Studio Candidate Test 1'
license = 'MIT'
long_description = readme + '\n\n' + changelog
url = 'https://undefined'

source_dir = 'source'

requirements = []
setup_requirements = []
test_requirements = []

setup(
    author=author,
    author_email=author_email,
    python_requires='>=3.7',
    classifiers=[
        'License :: Apple Internal',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
    description=description,
    entry_points={},
    install_requires=requirements,
    license=license,
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    name=name,
    packages=find_packages(source_dir),
    package_dir={'': source_dir},
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    url=url,
    zip_safe=False
)
