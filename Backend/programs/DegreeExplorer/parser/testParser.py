"""
This file contains the test cases for the parser.
"""
from Backend.programs.DegreeExplorer.parser.ExclusionParser import \
    ExclusionParser
from Backend.programs.DegreeExplorer.parser.PrereqParser import \
    PrereqParser
import unittest


class testExclusionParser(unittest.TestCase):
    def testNoneCase(self):
        parser = ExclusionParser("None", [])
        self.assertTrue(parser.checkCourseApproval())

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
        self.assertTrue(parser.checkCourseApproval())

        parser = ExclusionParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC148H5"])
        self.assertTrue(parser.checkCourseApproval())
        #
        parser = ExclusionParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC108H5", "CSC148H5"])
        self.assertFalse(parser.checkCourseApproval())

        parser = ExclusionParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC165H5"])
        self.assertFalse(parser.checkCourseApproval())


class testPreReqParser(unittest.TestCase):

    def testNoneCase(self):
        parser = PrereqParser("None", [])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("None", ["CSC108H5"])
        self.assertTrue(parser.evaluatePrereq())

    def testNonCompoundCase(self):
        parser = PrereqParser("CSC108H5", ["CSC108H5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5", ["CSC148H5"])
        self.assertFalse(parser.evaluatePrereq())

    def testCompoundCaseOR(self):
        parser = PrereqParser("CSC108H5 or CSC148H5", ["CSC108H5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5 or CSC148H5", ["CSC148H5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5 or CSC148H5", ["CSC108H5", "CSC148H5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5 or CSC148H5", ["CSC165H5"])
        self.assertFalse(parser.evaluatePrereq())

    def testCompoundCaseAND(self):
        parser = PrereqParser("CSC108H5 and CSC148H5", ["CSC108H5"])
        self.assertFalse(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5 and CSC148H5", ["CSC148H5"])
        self.assertFalse(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5 and CSC148H5", ["CSC108H5", "CSC148H5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("CSC108H5 and CSC148H5", ["CSC108H5", "CSC148H5", "CSC165H5"])
        self.assertTrue(parser.evaluatePrereq())


    def testCompoundCaseANDOR(self):
        parser = PrereqParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC108H5"])
        self.assertFalse(parser.evaluatePrereq())

        parser = PrereqParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC148H5"])
        self.assertFalse(parser.evaluatePrereq())

        parser = PrereqParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC108H5", "CSC148H5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("(CSC108H5 and CSC148H5) or CSC165H5", ["CSC165H5"])
        self.assertTrue(parser.evaluatePrereq())

    def testCompoundCaseCredits(self):
        parser = PrereqParser("4.0 credits", ["CSC108H5"])
        self.assertFalse(parser.evaluatePrereq())

        parser = PrereqParser("2.0 credits", ["CSC108Y5", "CSC148Y5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("2.0 credits", ["CSC108Y5", "CSC148H5"])
        self.assertFalse(parser.evaluatePrereq())

        parser = PrereqParser("2.0 credits in CSC", ["CSC108Y5", "CSC148Y5"])
        self.assertTrue(parser.evaluatePrereq())

        parser = PrereqParser("2.0 credits in CSC at the 100-level", ["CSC108Y5", "CSC148Y5"])
        self.assertTrue(parser.evaluatePrereq())
