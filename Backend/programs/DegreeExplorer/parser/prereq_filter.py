import csv
import re
from MyAcademia.parser.PrereqParser import PrereqParser

def read_csv():
    with open('/Scripts/course_data.csv',
              mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        course_data = {}
        for row in reader :
            course_data[row['course_code']] = row['pre_req']
    return course_data

course_data = read_csv()


def filter_none_pre_req():
    f = open("/Backend/programs/DegreeExplorer/parser/pre_req_out/none.txt", "w")
    for course in course_data:
        parser = PrereqParser(course_data[course], [])
        if parser.check_for_none_requirement():
            f.write(f"{course}: {course_data[course]}\n")
    f.close()

# NOTE: No course code also imples None and Grade 12
def filter_no_course_code_req():
    f = open(
        "/Backend/programs/DegreeExplorer/parser/pre_req_out/no_course_req.txt", "w")
    for course in course_data:
        parser = PrereqParser(course_data[course], [])
        if parser.check_for_no_course_code_req():
            if not parser.check_for_none_requirement():
                if not parser.check_for_garde12_req():
                    f.write(f"{course}: {course_data[course]}\n")
    f.close()

def filter_grade12_req():
    f = open("/Backend/programs/DegreeExplorer/parser/pre_req_out/grade12.txt", "w")
    for course in course_data:
        parser = PrereqParser(course_data[course], [])
        if parser.check_for_garde12_req():
            f.write(f"{course}: {course_data[course]}\n")
    f.close()

def filter_strctured_pre_reqs():
    f = open(
        "/Backend/programs/DegreeExplorer/parser/pre_req_out/structured.txt", "w")
    for course in course_data:
        parser = PrereqParser(course_data[course], [])
        if parser.check_for_structured_prereq():
            if not parser.check_for_none_requirement() and not parser.check_for_no_course_code_req() and not parser.check_for_garde12_req():
                f.write(f"{course}: {course_data[course]}\n")
    f.close()

def filter_credit_based_pre_reqs():
    f = open("/Backend/programs/DegreeExplorer/parser/pre_req_out/credits.txt", "w")
    for course in course_data:
        parser = PrereqParser(course_data[course], [])
        if parser.check_for_credits_in_prereq() and not parser.check_for_course_code():
            if not parser.check_for_none_requirement() and not parser.check_for_garde12_req():
                f.write(f"{course}: {course_data[course]}\n")

    # f = open("/Users/guninkakar/Desktop/GDSC/myAcademia/MyAcademia/parser/pre_req_out/credits.txt", "w")
    # for course in course_data:
    #     parser = PrereqParser(course_data[course], [])
    #     if parser.check_for_credits_in_prereq():
    #         if not parser.check_for_none_requirement() and not parser.check_for_no_course_code_req() and not parser.check_for_garde12_req():
    #             f.write(f"{course}: {course_data[course]}\n")


filter_none_pre_req()
filter_no_course_code_req()
filter_grade12_req()
filter_strctured_pre_reqs()

filter_credit_based_pre_reqs()
