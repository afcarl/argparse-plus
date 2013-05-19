# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]

setup( 
        name='argparse_plus',
        version='0.1.0',
        description='ArgumentParser Plus',
        long_description = open('README.rst').read(),
        author='Patrick Ng',
        author_email='pn.appdev@gmail.com',
        url='https://github.com/pnpnpn/argparse-plus',
        packages=['argparse_plus'],
        install_requires=[],
        #test_suite='tests',
        classifiers=CLASSIFIERS)


