import pymysql


connection = pymysql.connect(
    host='localhost',  # Hostname
    user='root',  # MySQL username
    password='utm@GDSC',  # MySQL password
    database='testDatabase'  # Database name
)


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
);
'''


# running the queries
cursor.execute(create_courseDescription)
cursor.execute(create_courses)
cursor.execute(create_programs)
cursor.execute(create_requirements)

# Commit the changes: This line essenitaly saves the changes and adds to
# the database, similar to git commit :)
connection.commit()

# ends the connection and closes the cursor
cursor.close()
connection.close()
