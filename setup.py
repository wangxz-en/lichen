#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='lichen',
    version='0.1',
    description="Tick-based online AI game",
    url='http://github.com/lucian1900/lichen',

    packages=find_packages(),
    install_requires=[
        'django==1.4',
        'south==0.7.4',
        'django-tastypie==0.9.11',
        'Twisted==12.0.0',
        'gunicorn==0.14.2',
    ],
    scripts=[
        'scripts/start-txproxy',
        'scripts/start-txwsgi',
        'scripts/stop-txproxy',
        'scripts/stop-txwsgi',
    ])
