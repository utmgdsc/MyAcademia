import requests
from pathlib import Path
import json
import argparse
import sys

from constants import allCoursesRe, allProgramsRe, requirementRe

addProgramPOSTHeader = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Content-Type": "text/plain",
    "DNT": "1",
    "Host": "degreeexplorer.utoronto.ca",
    "Origin": "https://degreeexplorer.utoronto.ca",
    "Referer": "https://degreeexplorer.utoronto.ca/degreeExplorer/planner",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-XSRF-TOKEN": "Vcs464vTo6UCHRjbIlLx8rMMBd8V8NIxVkLGnZGA5lU=",
    "Cookie": ""
}