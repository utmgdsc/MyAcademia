from bs4 import BeautifulSoup
import requests
import csv
with open('pre-req.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Program','Courses','Pre-Requisites'])
    #courses_prereq_dict = {}
    for i in range(6):
        URL=f'https://utm.calendar.utoronto.ca/program-search?page={i}'
        html_page = requests.get(URL).text
        soup = BeautifulSoup(html_page, 'lxml')
        program_pg = soup.find_all('div', class_='views-row')
        for i in range(1, len(program_pg), 2):
            # courses_prereq_dict={}
            program = program_pg[i]
            program_name = program.find('h2', class_='field-content').text.replace(" ", "")
            #print(program_name)
            if 'ComputerScience-Major(Science)'== program_name or 'MathematicalSciences-Major(Science)'==program_name or 'AppliedStatistics-Major(Science)'==program_name:
                list_URL=program.find_all('a')
                for url in list_URL:
                    text=url.text
                    #print(text)
                    if text== 'Computer Science' or text=='Mathematical Sciences' or text=='Statistics, Applied':
                        courses_prereq_dict={}
                        imp_url = 'https://utm.calendar.utoronto.ca/'+url['href']
                        #print(imp_url)
                        program_page=requests.get(imp_url).text
                        soup2=BeautifulSoup(program_page,'lxml')
                        # print(soup2)
                        if text== 'Computer Science':
                            section_courses=soup2.find('div',class_="view view-courses-view view-id-courses_view view-display-id-block_1 js-view-dom-id-2f44f26bc9f01bd5887796eb965882806adeb88d5d80e0bd5328c7dccf830861")
                        elif text== 'Mathematical Sciences':
                            section_courses=soup2.find('div',class_="view view-courses-view view-id-courses_view view-display-id-block_1 js-view-dom-id-76af5a138afd8b3169e53d140bbe9f91c395bfcdf6e519847bdb9faa29a69d0d")
                        elif text == 'Statistics, Applied':
                            section_courses=soup2.find('div',class_="view view-courses-view view-id-courses_view view-display-id-block_1 js-view-dom-id-0c0b2f5c774411c917b994fd3f74ebef86cd4d64d389336eb56705469d3dbdd4")

                        filtered_section_course=section_courses.find('div',class_='view-content')
                        individual_course=filtered_section_course.find_all('div')
                        for courses in individual_course:
                           if courses.find('h3', class_="js-views-accordion-group-header"):
                                course_name=courses.find('h3', class_="js-views-accordion-group-header").text.split("•")[0]
                                courses_prereq_dict[course_name]=None

                           if courses.find('span',class_="views-field views-field-field-prerequisite"):
                               span_ele=courses.find('span',class_="views-field views-field-field-prerequisite")
                               pre_req_ele=span_ele.find('span',class_="field-content").text
                               #print(pre_req_ele)
                               if courses_prereq_dict[course_name] is None:
                                   courses_prereq_dict[course_name]=pre_req_ele
                        for key in courses_prereq_dict:
                            writer.writerow([text,key,courses_prereq_dict[key]])








