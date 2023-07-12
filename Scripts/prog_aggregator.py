#!/usr/bin/env python3

import json
import glob
import argparse
from pathlib import Path
import re

from constants import allCoursesRe, allProgramsRe, requirementRe
"""
 A script that Aggregates and cleans program JSON objects downloaded from https://degreeexplorer.utoronto.ca/.
"""
# Set up argument parsing
parser = argparse.ArgumentParser(description="Aggregates and cleans program JSON objects downloaded from https://degreeexplorer.utoronto.ca/.")
parser.add_argument("--p_jsons_dir", type=str, help="path to directory to read downloaded program JSONs from. default: ./program_data", default="./program_data", metavar="dir")
parser.add_argument("--p_aggr_file", type=argparse.FileType("w"), help="path to file to write aggregated programs into. default: ./aggregated_programs.json", default="./aggregated_programs.json", metavar="file")
parser.add_argument("--debug", help="include to pretty-print JSON. Useful for debugging.", action="store_true")

# Dict to hold final aggregated JSON obj
aggregated_programs = {}
a = []

if __name__ == "__main__":
    args = parser.parse_args()

    print("Starting program aggregation...")

    attempted = 0

    for programFile in glob.glob(f"{args.p_jsons_dir}/*.json"):
        attempted += 1

        # Read file into dict
        with open(programFile) as f:
            programObj = json.load(f)

        # From the top level, remove everything except these two
        for key in list(programObj.keys()):
            if key not in ["title", "detailAssessments"]:
                del programObj[key]

        # # For each requirement, first bring the embedded requirement object a level higher and make it a dict instead of a list
        newReqs = {}
        for reqObj in programObj["detailAssessments"]:
            # Bring the main requirement object one level higher
            reqObj['requirement']['count'] = reqObj['credits']['requiredCredits']
            reqObj = reqObj["requirement"]
            # Extract some useful info
            reqID = reqObj["shortIdentifier"][1:-1]
            displayPrefix = reqObj["displayPrefix"]
            connector = reqObj["subItemConnectorString"]
            displaySuffix = reqObj["displaySuffix"]
            type_ = reqObj["type"]
            # We need the actual codes of each requisiteItem to make the display string
            requisiteCodes = []

            # For each requisite item, we only need the code and the type of the code i.e. course, program, or category, or another prereq. We will group them via these labels.
            courses = []
            programs = []  # There are actually no programs in any of the requirements, but this is just left in for completion's sake.
            categories = []
            dependentReqs = []


