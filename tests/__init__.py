# tests
# Testing for the PyCellularAutomata package
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jan 31 09:25:17 2014 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing for the PyCellularAutomata package
"""

##########################################################################
## Imports
##########################################################################

import os
import unittest

##########################################################################
## TestCases
##########################################################################

class InitializationTest(unittest.TestCase):

    def test_initialization(self):
        """
        Test a simple world fact to kick off testing
        """
        self.assertEqual(2**3, 8)

    def test_import(self):
        """
        We are able to import our packages
        """
        try:
            import pyca
        except ImportError:
            self.fail("Unable to import the pyca module!")
