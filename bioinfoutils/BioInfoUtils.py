# -*- coding: utf-8 -*-

from bioinfoutils.core import *

# Main entry point in library

class BioInfoUtils(object):
    """docstring for BioInfoUtils."""
    def __init__(self):
        super(BioInfoUtils, self).__init__()
        self.algorithms = algorithms(self)
        self.data       = data(self)
        self.io         = io(self)
