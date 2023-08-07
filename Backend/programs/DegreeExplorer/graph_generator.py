import csv
import re
class course:

    # ['course_code', 'title', 'description', 'credit', 'distribution', 'recommended_prep', 'pre_req', 'exclusions', 'program_area']
    def __init__(self, course_code, title, description, credit, distribution, pre_req, exclusions):
        self.course_code = course_code
        self.title = title
        self.description = description
        self.credit = credit
        self.distribution = distribution
        self.pre_req = pre_req
        self.exclusions = exclusions

course_list = {}
utmCourseRegex = re.compile(r'[A-Z]{3}[0-9]{3}H5')
def generate_course_list():
    with open('/Users/guninkakar/Desktop/GDSC/myAcademia/MyAcademia/Scripts/course_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            course_list[row['course_code']] = course(row['course_code'], row['title'], row['description'], row['credit'], row['distribution'], row['pre_req'], row['exclusions'])

generate_course_list()
# print(len(course_list))
cs_minor_courses = ["CSC108H5","CSC148H5","CSC207H5","MAT102H5","CSC236H5","CSC209H5","CSC263H5","CSC258H5","MAT135H5","MAT136H5","MAT232H5","MAT223H5","CSC311H5","CSC369H5","CSC373H5","CSC343H5","CSC363H5","CSC358H5","CSC413H5", "MAT139H5","MAT159H5"]

def get_course_objects(list_of_courses):
    course_objects = []
    for course in list_of_courses:
        course_objects.append(course_list[course])
    return course_objects

cs_minor = get_course_objects(cs_minor_courses)


class graph:
    def __init__(self):
        self.adj_list = {}
        self.visited = {}


    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)


    def build_graph(self, courses):
        for course in courses:
            self.adj_list[course.course_code] = []

        for course in courses:
            if course.pre_req != "None" or "Grade 12" in course.pre_req:
                # need to find the kind of pre_req
                # assuming here to be structured
                # REGEX
                courses_in_pre_req = re.findall(utmCourseRegex, course.pre_req)
                for c in courses_in_pre_req:
                    self.add_edge(c, course.course_code)


    def print_graph(self):
        for course in self.adj_list:
            print(course, end=" ")
            for c in self.adj_list[course]:
                print(c, end=" ")
            print()



graph = graph()
graph.build_graph(cs_minor)
graph.print_graph()
