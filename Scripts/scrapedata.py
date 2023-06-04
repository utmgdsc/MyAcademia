from bs4 import BeautifulSoup
import requests
import csv
from Scripts import databaseFiller

'''
Created a class for the course data with the properties: Course Code, Course Title, Credit, Distribution, 
Recommended Prep, Pre Requisites, Exclusion
'''
class CourseData:
    code: str
    title: str
    credit: str
    distribution: str
    recommended_prep: str
    pre_req: str
    exclusion: str
    description: str
    def __init__(self,code,title,credit,distribution,recommended_prep,pre_req,exclusion,description):
        self.code=code
        self.title=title
        self.credit=credit
        self.distribution=distribution
        self.recommended_prep=recommended_prep
        self.pre_req=pre_req
        self.exclusion=exclusion
        self.description=description

    def populate_data(self):
        """
        Scrape data from the uoft academic calendar website and populate into a csv file
        """
        with open('data.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Preparing the CSV file Columns
            writer.writerow(
                ['Course Code', 'Course Title','Course Description', 'Credit', 'Distribution', 'Recommended Prep', 'Pre Requisites',
                 'Exclusion'])
            for i in range(79):
                URL = f'https://utm.calendar.utoronto.ca/course-search?page={i}'
                html_page = requests.get(URL).text
                soup = BeautifulSoup(html_page, 'lxml')
                course_section_tab = soup.find('div', class_='view-content')
                courses = course_section_tab.find_all('div', class_='views-row')
                for course in courses:
                    # Course Code and Title
                    if course.find('h3',class_='js-views-accordion-group-header'):
                        course_code_title = course.find('h3',class_='js-views-accordion-group-header').text.split('•')
                        self.code=course_code_title[0]
                        self.title=course_code_title[1]
                       #Course Credit
                        if self.code[-3]== 'H':
                            self.credit='0.5'
                        elif self.code[-3]== 'Y':
                            self.credit='1.0'
                    else:
                        continue
                    # Course Description
                    if course.find('div',class_="views-field views-field-field-desc"):
                        div_elem=course.find('div',class_="views-field views-field-field-desc")
                        self.description=div_elem.find('div',class_='field-content').find('p').text
                    else:
                        self.description='None'

                    # Course Distribution
                    if course.find('span',class_="views-field views-field-field-distribution-requirements"):
                        span_elem=course.find('span',class_="views-field views-field-field-distribution-requirements")
                        self.distribution=span_elem.find('span',class_='field-content').text
                    else:
                        self.distribution='None'

                    #Course Exclusion
                    if course.find('span',class_="views-field views-field-field-exclusion"):
                        span_elem=course.find('span',class_="views-field views-field-field-exclusion")
                        self.exclusion=span_elem.find('span',class_='field-content').text
                    else:
                        self.exclusion='None'
                    #Course Pre Requisites
                    if course.find('span',class_="views-field views-field-field-prerequisite"):
                        span_elem=course.find('span',class_="views-field views-field-field-prerequisite")
                        self.pre_req=span_elem.find('span',class_='field-content').text
                    else:
                        self.pre_req='None'

                    #Course Recommended Prep
                    if course.find('span',class_="views-field views-field-field-recommended-preparation"):
                        span_elem=course.find('span',class_="views-field views-field-field-recommended-preparation")
                        self.recommended_prep=span_elem.find('span',class_='field-content').text
                    else:
                        self.recommended_prep='None'

                    # writer.writerow([self.code, self.title,self.description,self.credit, self.distribution, self.recommended_prep,
                    #               self.pre_req, self.exclusion])
                    databaseFiller.fillCourseDatabase([self.code, self.title, self.credit, self.distribution , self.recommended_prep,
                                                       self.pre_req, self.exclusion])






course_data=CourseData('','','','','','','','')
course_data.populate_data()



