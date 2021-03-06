#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django==2.0.2',
    'dj-database-url==0.4.2',
    'django-braces==1.12.0',
    'django-compressor==2.2',
    'django-configurations==2.0',
    'django-model-utils==3.1.1',
    'django-sass-processor==0.5.8',
    'envdir==0.7',
    'libsass==0.13.7',
    'psycopg2==2.7.4',
    'pytz==2018.3',
]

setup(
    name='bureau',
    version='0.1.0',
    description='bureau is a django based (home-)office solution.',
    long_description=read(BASE_DIR, 'README.rst'),
    author='Max Brauer',
    author_email='max@max-brauer.de',
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],
    install_requires=requires,
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
