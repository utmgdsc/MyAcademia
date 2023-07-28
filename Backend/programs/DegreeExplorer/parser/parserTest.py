"""
This file contains the test cases for the parser.
"""
from Backend.programs.DegreeExplorer.parser.ExclusionParser import \
    ExclusionParser
import unittest


class testExclusionParser(unittest.TestCase):
    def testBasic(self):
        parser = ExclusionParser("CSC108H5", ["CSC108H5"])
        self.assertFalse(parser.checkCourseApproval())

    def testBasic2(self):
        parser = ExclusionParser("CSC108H5", [])
        self.assertTrue(parser.checkCourseApproval())

    def testBasic3(self):
        parser = ExclusionParser("CSC108H5 or CSC148H5", ["MAT102H5"])
        self.assertTrue(parser.checkCourseApproval())
