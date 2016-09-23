# -*- coding: utf-8 -*-
# 2016/9/23 10:27
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
from setuptools import setup, find_packages

setup(
    name = 'pytesser3',
    version = '1.0.1',
    keywords = ('pytesser', 'support 3.x'),
    description = 'modify and let it support 3.x',
    license = 'MIT License',
    install_requires = ['requests'],

    author = 'LouisSong',
    author_email = 'slysly759@gmail.com',

    packages = find_packages(),
    package_data = {
        # If any package contains *.txt files, include them:
        '': ['*'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
    },


    platforms = 'any',
)