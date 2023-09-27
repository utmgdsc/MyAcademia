# MyAcademia
---
## Description
MyAcademia is a website that will be a tool for UTM students for course enrollment. It will aid them during their course selection and planning their degree. There will be 3 main features for this web application:
1. Course Search: The web application will implement a feature allowing the user to search for specific UTM courses based on specific criteria such as Course Code, Prerequisites, Rating etc. The application will display a list of relevant courses based on the search criteria. Each item on the list will be a hyperlink linking to the appropriate course’s info page where a user can view important course information such as Course Code, Course Description, Distribution, Course reviews etc. 

2. Course Review: The web application allows the user to look at online reviews of a course and also add reviews by themselves. 

3. Study Plan Generator: The web application allows the user to plan out their degree based on their choice of program. This includes generating suggestions that take into account previously taken courses and various other factors
---

## Deployment
Currently, the application hasn’t been hosted on any server. However, below are the steps to set up the application on a user’s local computer. Please note that these steps do not include populating the database with User Reviews as these are not stored in any file and are not scraped from the internet.  

Prerequisites
- Python - https://www.python.org/downloads/
- Npm - https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
- ReactJS 


### Backend Setup
First create a virtual python environment. Run the command python -m venv “path” where “path” is the path where you want to store the virtual environment
Activate the new virtual environment. Use the command source path_to_venv/bin/activate
Use pip to install the following (pip install name_of_library)
- Django
- Djoser
- Djangorestframework
- bs4
- lxml
- tensorflow (if wanting to add scraped reddit reviews into database)
- praw
- profanity
- pandas
- scripts
- django-cors-headers
- Django-extensions


Clone the github repository : 
```
git clone https://github.com/utmgdsc/MyAcademia.git
```
Navigate to the Scripts directory in the project:
```
 cd MyAcademia/Scripts
```
Run the following scripts
- scrapedata.py - generates a csv with list of course. csv is titled course_data.csv
- redditreviewscraper.py - generates a csv with list of course reviews scraped from reddit. csv is titled courses_reviews.csv Please note this will take a while to get the list for all courses. We recommend running it for a few mins to scrape data for the first few courses. The script will automatically print the PID of the process which you can use to terminate the process if required. Ctrl C should work as well
Navigate to the backend directory in the command line. You should be able to see a manage.py file
Run the makemigrations command (python manage.py makemigrations) followed by the migrate command (python mange.py migrate). 
Run the following commands (in order) to load data into the database:
```
python manage.py load_courses <path_to_course_data.csv>
python manage.py load_online_reviews <path_to_courses_reviews.csv>
python manage.py load_programs <aggregated_programs.json> (located in the scripts directory)
python manage.py load_professors <professors_data.csv> (located in the scripts directory)
```
The backend is now setup

### Frontend setup
Navigate to the frontend directory (MyAcademia/Frontend/frontend)
Make sure there does not exist a node_modules folder. If there does, remove it (rm -r node_modules)
Run the command:
```
npm start
```

The frontend is now setup

### Running the app
First activate the virtual environment you had setup for the backend. 
Navigate to the backend directory and run the server (python manage.py runserver)
On a separate terminal, navigate to the frontend directory and start the frontend server :
```npm start
```

The app is now up and running. Navigate to localhost:3000 on your browser to see the functional web application. 
