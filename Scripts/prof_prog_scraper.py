from bs4 import BeautifulSoup
import requests
import csv

"""
A script to scrape the Professor name and their department from UTM academic calendar website
"""


class ProfessorsData:
    professors: list[str]
    department: str

    def __init__(self, department):
        self.professors = []
        self.department = department

    def strip_all(self):
        for i in range(len(self.professors)):
            self.professors[i] = self.professors[i].strip()
        self.department = self.department.strip()

    def populate_data(self):
        dict_tracket = {}
        academic_calendar_url = 'https://utm.calendar.utoronto.ca/list-program-areas'
        html_page = requests.get(academic_calendar_url).text
        soup = BeautifulSoup(html_page, 'lxml')
        program_area_tab = soup.find_all('table', role='presentation')[:-1]
        for program_area in program_area_tab:
            table_body = program_area.find('tbody')
            anchor = table_body.find_all('a')
            for a in anchor:
                self.department = a.text
                copy = self.department.replace(" ", "-")
                if copy in dict_tracket:
                    continue
                else:
                    dict_tracket[copy] = 1
                print(copy)
                # print(self.department)
                if copy:
                    program_url = 'https://utm.calendar.utoronto.ca/section/' + copy
                    html_page2 = requests.get(program_url).text
                    if html_page2:
                        soup2 = BeautifulSoup(html_page2, 'lxml')
                        if soup2.find('div', class_='views-field views-field-body'):
                            div_tab = soup2.find('div', class_='views-field views-field-body')
                            if div_tab.find('div', class_='field-content'):
                                inner_div = div_tab.find('div', class_='field-content')
                                professors_tab = inner_div.find('p')
                                if professors_tab:
                                    lines = professors_tab.text.split('\n')
                                    professors = []
                                    for line in lines:
                                        if line.strip().startswith(('Professors Emeriti', 'Professors')):
                                            continue
                                        if line.__contains__('Chair'):
                                            break
                                        professors.append(line)

                                    for professor in professors:
                                        print(professor)


if __name__ == '__main__':
    prof_data = ProfessorsData("")
    prof_data.populate_data()
