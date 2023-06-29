#######
# IMPORT PACKAGES
#######

import praw
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

from Scripts import databaseFiller
#from Scripts import databaseFiller
import prawcore
import random
from profanity import profanity
#Using the profanity package to censor the reviews
# Acessing the reddit api

list_courses = []
reddit = praw.Reddit(client_id="SMYL-lb2BhaNvaAi8SwVkw",  # my client id
                     client_secret="PFnA97kUL64vgAdWK9cnRxGWtM6siQ",  # your client secret
                     user_agent="utmreviewscraper",  # user agent name
                     username="myacademia392",  # your reddit username
                     password="akadgu392")  # your reddit password

# Print pid. Used to kill the process.
import os
print(os.getpid())
#Scraping the academic calendar website for course codes
for i in range(80):
    URL = f'https://utm.calendar.utoronto.ca/course-search?page={i}'
    html_page = requests.get(URL).text
    soup = BeautifulSoup(html_page, 'lxml')
    course_section_tab = soup.find('div', class_='view-content')
    courses = course_section_tab.find_all('div', class_='views-row')
    for course in courses:
        # Course Code and Title
        if course.find('h3', class_='js-views-accordion-group-header'):
            course_code_title = course.find('h3', class_='js-views-accordion-group-header').text.split('•')
            code = course_code_title[0]
            list_courses.append(code)
#Scraping Reddit Reviews for each course
with open('courses_reviews.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["course_code","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]) # For the 10 reviews
    for course in list_courses:
        reddit_coursecode = course[0:len(course) - 3].strip()
        subreddit_name='UTM'
        list_reviews=[]
        subreddit = reddit.subreddit(subreddit_name)
        reviews=subreddit.search(query=reddit_coursecode, sort='relevance',time_filter='all', limit=15)
        for index, review in enumerate(reviews, start=1):
            review.comments.replace_more(limit=None)  # Retrieve all comments, including nested ones
            comments = [comment for comment in review.comments if comment.parent_id.startswith('t3_')][
                       :25]  # Get the 25 -level comments based on relevance.

            for index, comment in enumerate(comments, start=1):
                body = comment.body
                #Check to see if comments contain swear words and censor them
                if profanity.contains_profanity(body):
                    body=profanity.censor(body)
                body = body.replace('&#x200B;','').strip('\n')
                if len(body)>100 :
                    if len(list_reviews)>=20:
                        break
                    else:
                        list_reviews.append(body.strip())
        #Using 10 Random Reviews out of 20 to remove bias
        random.shuffle(list_reviews)
        random_reviews_list = list_reviews[0:10]
        # Populate with empty strings if there are less than 10 reviews
        if(len(random_reviews_list)<10):
            for i in range(10-len(random_reviews_list)):
                random_reviews_list.append("")
        writer.writerow([course,random_reviews_list[0], random_reviews_list[1], random_reviews_list[2], 
                         random_reviews_list[3], random_reviews_list[4], random_reviews_list[5], 
                         random_reviews_list[6], random_reviews_list[7], random_reviews_list[8], random_reviews_list[9]])









