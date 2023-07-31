"""
This file contains the test cases for the parser.
"""
from Backend.programs.DegreeExplorer.parser.ExclusionParser import \
    ExclusionParser
import unittest


class testExclusionParser(unittest.TestCase):
    def testNoneCase(self):
        # case1: No course and no exclusions
        parser = ExclusionParser("None", [])
        self.assertTrue(parser.checkCourseApproval())

        # case2: some course and no exclusions
        parser = ExclusionParser("None", ["CSC108H5"])
        self.assertTrue(parser.checkCourseApproval())

    def testNonCompoundCase(self):
        parser = ExclusionParser("CSC108H5", ["CSC108H5"])
        self.assertFalse(parser.checkCourseApproval())

    def testCompoundCaseOR(self):
        parser = ExclusionParser("CSC108H5 or CSC148H5", ["CSC108H5"])
        self.assertFalse(parser.checkCourseApproval())

        parser = ExclusionParser("CSC108H5 or CSC148H5", ["CSC148H5"])
        self.assertFalse(parser.checkCourseApproval())

        parser = ExclusionParser("CSC108H5 or CSC148H5", ["CSC108H5", "CSC148H5"])
        self.assertFalse(parser.checkCourseApproval())

        parser = ExclusionParser("CSC108H5 or CSC148H5", ["CSC165H5"])
        self.assertTrue(parser.checkCourseApproval())

    def testCompoundCaseAND(self):
        parser = ExclusionParser("CSC108H5 and CSC148H5", ["CSC108H5"])
        self.assertTrue(parser.checkCourseApproval())

        parser = ExclusionParser("CSC108H5 and CSC148H5", ["CSC148H5"])
        self.assertTrue(parser.checkCourseApproval())

        parser = ExclusionParser("CSC108H5 and CSC148H5", ["CSC108H5", "CSC148H5"])
        self.assertFalse(parser.checkCourseApproval())

    def testCompoundCaseANDOR(self):
        parser = ExclusionParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC108H5"])
        self.assertFalse(parser.checkCourseApproval())

        parser = ExclusionParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC148H5"])
        self.assertFalse(parser.checkCourseApproval())
        #
        # parser = ExclusionParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC108H5", "CSC148H5"])
        # self.assertFalse(parser.checkCourseApproval())


class testPreReqParser(unittest.TestCase):

    def testBasic(self):
        pass
