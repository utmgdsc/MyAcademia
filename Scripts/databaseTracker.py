"""
This script will help to create all the tables needed to
store the data for the MyAcademia application.
"""
import pymysql


def trackDatabase():
    """
    This function will help to create all the tables needed to
    store the data for the MyAcademia application.
    """
    # making connection to the database
    connection = pymysql.connect(host='localhost', user='root',
                                 password='utm@GDSC',
                                 database='testDatabase')

    # this helps to add quires
    cursor = connection.cursor()

    # create courseDescription table
    create_courseDescription = '''CREATE TABLE IF NOT EXISTS courseDescription (
        course_code VARCHAR(100) NOT NULL PRIMARY KEY,
        Description VARCHAR(2500) NULL
    );
     '''

    # create courses table
    create_courses = '''CREATE TABLE IF NOT EXISTS courses (
        course_code      VARCHAR(100)  NOT NULL PRIMARY KEY,
        title            VARCHAR(200)  NOT NULL,
        credit           VARCHAR(10)   NULL,
        distribution     VARCHAR(100)  NULL,
        recommended_prep VARCHAR(500)  NULL,
        prerequisites    VARCHAR(500)  NULL,
        exclusions       VARCHAR(500)  NULL,
        description      VARCHAR(1000) NULL
    );'''

    # create programs table
    create_programs = '''CREATE TABLE IF NOT EXISTS programs (
        program_ID        INT          NOT NULL PRIMARY KEY,
        program_name      VARCHAR(100) NULL,
        type_of_program   VARCHAR(50)  NULL
    );
    '''

    # create requirements table
    create_requirements = '''CREATE TABLE IF NOT EXISTS requirements (
        requirement_ID   INT           NOT NULL PRIMARY KEY,
        requirement      VARCHAR(2000) NOT NULL,
        program_ID       INT           NOT NULL,
        CONSTRAINT requirements_programs_program_ID_fk
            FOREIGN KEY (program_ID) REFERENCES programs (program_ID)
    ); '''

    # create users table
    create_users = '''CREATE TABLE IF NOT EXISTS myAcademia_users (
        `UofT Email` VARCHAR(25)  NOT NULL PRIMARY KEY,
        Name         VARCHAR(50)  NOT NULL,
        userName     VARCHAR(8)   NOT NULL,
        Password     VARCHAR(256) NOT NULL,
        CONSTRAINT myAcademia_users_pk UNIQUE (userName)
    ); '''

    # create professors table
    create_professors = ''' CREATE TABLE IF NOT EXISTS professor (
        prof_ID         INT          NOT NULL PRIMARY KEY,
        professor_name  VARCHAR(400) NOT NULL,
        department      VARCHAR(100) NULL
    ); '''

    # create onlineReviews Table
    create_onlineReviews = '''CREATE TABLE IF NOT EXISTS onlineReviews (
        `review ID`                VARCHAR(100)  NOT NULL PRIMARY KEY,
        `sentiment analysis value` INT           NULL,
        reviews                    VARCHAR(2500) NULL,
        `course code`              VARCHAR(100)  NOT NULL,
        CONSTRAINT `onlineReviews_courses_course_code_fk`
            FOREIGN KEY (`course code`) REFERENCES courses (course_code)
    );
     '''

    # create userReviews Table
    create_userReviews = '''CREATE TABLE IF NOT EXISTS userReviews (
        `review ID`     VARCHAR(100)  NOT NULL,
        review          VARCHAR(1000) NULL,
        rating          INT           NULL,
        `course code`   VARCHAR(100)  NOT NULL,
        userName        VARCHAR(100)  NOT NULL,
        professor       VARCHAR(100)  NULL,
        `professor ID`  INT           NOT NULL,
        CONSTRAINT course_code
            FOREIGN KEY (`course code`) REFERENCES courses (course_code),
        CONSTRAINT userName
            FOREIGN KEY (userName) REFERENCES myAcademia_users (userName),
        CONSTRAINT userReviews_professor_prof_ID_fk
            FOREIGN KEY (`professor ID`) REFERENCES professor (prof_ID)
    );
     '''

    # running the queries!!
    cursor.execute(create_courseDescription)
    cursor.execute(create_courses)
    cursor.execute(create_programs)
    cursor.execute(create_requirements)
    cursor.execute(create_users)
    cursor.execute(create_professors)
    cursor.execute(create_onlineReviews)
    cursor.execute(create_userReviews)

    # Commit the changes: This line essentially saves the changes and adds to
    # the database, similar to git commit :)
    connection.commit()

    # ends the connection and closes the cursor
    cursor.close()
    connection.close()
