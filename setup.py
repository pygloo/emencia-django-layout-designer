#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
from setuptools import setup, find_packages

version = '0.1.0'

# prepare long description
f = open('README')
LONG_DESCRIPTION = f.read().strip()
f.close()

setup(
    name='emencia-django-layout-designer',
    version=version,
    description='emencia-django-layout-designer',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'Environment :: Web Environment',
    ],
    keywords='edn, emencia-django-newsletter, django',
    author='Pigout Florent',
    author_email='florent.pigout@gmail.com',
    url='https://github.com/pygloo/emencia-django-layout-designer',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=[
        'emencia',
        'emencia.django',
        'emencia.django.layout',
        'emencia.django.layout.designer'
        ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
        'south',
        'emencia.django.newsletter'
        ],
    setup_requires=[],
)

