import pymysql
import databaseFiller
import databaseTracker
from Scripts.scrapedata import CourseData

"""
This script will be used to setup the database for the MyAcademia application
especially when any changes are made to keep the team members updated.
"""


def emptyDatabase():
    """
    The purpose of this function is to empty the database.
    """
    # todo: need to figure out fetchall
    pass


if __name__ == "__main__":
    databaseTracker.trackDatabase()
    # databaseFiller.fillCourseDatabase()
    course_data=CourseData('','','','','','','','')
    course_data.populate_data()
