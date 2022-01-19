#!/usr/bin/env python

from setuptools import setup

setup(name='matheval',
      version='0.1',
      requires=['flask', 'pytest', 'gunicorn'],
      setup_requires=['pytest-runner'],
      packages=['matheval']
     )
