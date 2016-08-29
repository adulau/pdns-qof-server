#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='qos-server',
    version='1.0',
    author='Alexandre Dulaunoy',
    author_email='alexandre.dulaunoy@circl.lu',
    maintainer='Alexandre Dulaunoy',
    url='https://github.com/adulau/pdns-qof-server',
    description='pdns-qof server is a "Common Output Format" compliant passive DNS query interface',
    packages=find_packages(),
    entry_points={'console_scripts': ['qos-server = qos_server:main']},
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
    ],
    install_requires=[
        'tornado',
        'redis',
    ]
)
