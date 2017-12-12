# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_DIR, 'README.rst')) as f:
    readme = f.read()

with open(os.path.join(BASE_DIR, 'LICENSE')) as f:
    license = f.read()

setup(
    name='entice-helper',
    version='0.1.0',
    description='helper for entice-bot to actually invite users to groups',
    url='https://github.com/entice-tg/entice-helper',
    long_description=readme,
    author='Sam Wilson',
    author_email='tecywiz121@hotmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),

    extras_require={
        'dev': [
            'tox>=2.9.1,<3.0.0',
        ]
    }
)
