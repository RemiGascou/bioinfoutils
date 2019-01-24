# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name         = 'bioinfoutils',
    version      = '0.1.2',
    description  = 'Basic tools needed in bioinformatics',
    url          = 'http://github.com/Remigascou/bioinfoutils',
    author       = 'Remi GASCOU',
    author_email = 'remi.gascou@gmail.com',
    license      = 'GPL2',
    packages     = [
        'bioinfoutils',
        'bioinfoutils/core'
    ],
    zip_safe     = False
)
