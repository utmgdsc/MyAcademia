import csv
import re

from Backend.programs.DegreeExplorer.parser.PrereqParser import PrereqParser

utmCourseRegex = re.compile(r'[A-Z]{3}[0-9]{3}H5')


class course:
    def __init__(self, course_code, title, description, credit, distribution,
                 pre_req, exclusions):
        self.course_code = course_code
        self.title = title
        self.description = description
        self.credit = credit
        self.distribution = distribution
        self.pre_req = pre_req
        self.exclusions = exclusions


"""
This class will keep track of the all the courses in the graph.
"""


class Vertex:
    def __init__(self, course):
        self.level = 0
        self.visited = False
        self.course = course

    def visited(self):
        self.visited = True


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        self.vertex_by_level = {}

    def add_edge(self, u, v):  # edge from u ---> v
        if u is None and v is not None:
            self.adj_list[v] = []
            if v.level not in self.vertex_by_level:
                self.vertex_by_level[v.level] = [v]
            else:
                self.vertex_by_level[v.level].append(v)
            return
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v is not None:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if v.level < u.level + 1:
                if v in self.vertex_by_level[v.level]:
                    self.vertex_by_level[v.level].remove(v)
                v.level = u.level + 1
            if v.level not in self.vertex_by_level:
                self.vertex_by_level[v.level] = [v]
            else:
                self.vertex_by_level[v.level].append(v)

    def build_graph(self):
        for vertex in self.vertices:
            if not (self.vertices[vertex].course.pre_req == "None" or "Grade 12" in self.vertices[vertex].course.pre_req):
                courses_in_pre_req = re.findall(utmCourseRegex, self.vertices[vertex].course.pre_req)
                for course_new in courses_in_pre_req:
                    try:
                        vertex2 = self.vertices[course_new]
                    except:
                        continue
                    self.add_edge(vertex2,self.vertices[vertex])
            else:
                self.add_edge(None, self.vertices[vertex])

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex.course.course_code," : ",end=" ")
            for v in self.adj_list[vertex]:
                print(v.course.course_code, end=" ")
            print()

    def print_vertex_by_level(self):
        for level in self.vertex_by_level:
            print(level, end=" ")
            for vertex in set(self.vertex_by_level[level]):
                print(vertex.course.course_code, end=" ")
            print()

    def suggestCourses(self):
        suggested_courses = []
        isLevelComplete = False
        for level in self.vertex_by_level:
            if isLevelComplete:
                break
            for vertex in self.vertex_by_level[level]:
                if vertex.visited:
                    for v in self.adj_list[vertex]:
                        if not v.visited:
                            suggested_courses.append(v)
                else:
                    isLevelComplete = True
                    suggested_courses.append(vertex)
        for val in suggested_courses:
            parser = PrereqParser(val.course.pre_req, [])
            if not parser.evaluatePrereq():
                suggested_courses.remove(val)
        for val in suggested_courses:
            print(val.course.course_code)
        return suggested_courses

course_list = {}


def generate_course_list():
    with open(
            '/Users/guninkakar/Desktop/GDSC/myAcademia/MyAcademia/Scripts/course_data.csv',
            newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            course_list[row['course_code']] = course(row['course_code'],
                                                     row['title'],
                                                     row['description'],
                                                     row['credit'],
                                                     row['distribution'],
                                                     row['pre_req'],
                                                     row['exclusions'])


generate_course_list()

cs_minor_courses = ["CSC108H5", "CSC148H5", "MAT102H5", "CSC207H5", "CSC236H5",
                    "CSC209H5", "CSC263H5", "CSC258H5", "MAT135H5", "MAT136H5",
                    "MAT232H5", "MAT223H5", "CSC369H5", "CSC373H5",
                    "CSC343H5", "CSC363H5", "CSC358H5", "MAT139H5",
                    "MAT159H5"]
#
# cs_minor_courses = ["CSC108", "CSC148", "MAT102", "CSC207", "CSC236", "CSC209", "CSC263", "CSC258", "MAT135", "MAT136", "MAT232", "MAT223", "CSC311", "CSC369", "CSC373", "CSC343", "CSC363", "CSC358", "CSC413", "MAT139", "MAT159"]



def get_course_objects(list_of_courses):
    course_objects = []
    for course in list_of_courses:
        course_objects.append(course_list[course])
    return course_objects

smth =  ["CSC104H5", "CSC108H5", "CSC148H5", "CSC199H5", "CSC207H5", "CSC209H5", "CSC236H5", "CSC258H5", "CSC263H5", "CSC290H5", "CSC299Y5", "CSC300H5", "CSC301H5", "CSC309H5", "CSC310H5", "CSC311H5", "CSC318H5", "CSC322H5", "CSC324H5", "CSC333H5", "CSC338H5", "CSC343H5", "CSC347H5", "CSC358H5", "CSC363H5", "CSC367H5", "CSC369H5", "CSC373H5", "CSC375H5", "CSC376H5", "CSC384H5", "CSC389H5", "CSC392H5", "CSC393H5", "CSC397H5", "CSC398H5", "CSC399Y5", "CSC404H5", "CSC409H5", "CSC413H5", "CSC415H5", "CSC420H5", "CSC422H5", "CSC423H5", "CSC427H5", "CSC428H5", "CSC458H5", "CSC469H5", "CSC475H5", "CSC476H5", "CSC477H5", "CSC478H5", "CSC479H5", "CSC488H5", "CSC490H5", "CSC492H5", "CSC493H5", "CSC496H5", "CSC497H5", "CSC498H5", "CSC499Y5","MAT102H5","MAT135H5","MAT136H5","MAT223H5","MAT232H5"]

cs_minor = get_course_objects(cs_minor_courses)

vertices = {}
for course in cs_minor:
    vertices[course.course_code] = Vertex(course)
graph = Graph(vertices)
graph.build_graph()
for vertex in graph.vertex_by_level[0]:
    vertex.visited = True
# graph.print_graph()
# graph.print_vertex_by_level()
graph.suggestCourses()


# print("[", end="")
# for i in course_list:
#     if "CSC" in i:
#         print("\"" + i + "\",", end=" ")

