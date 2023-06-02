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

# Execute the SQL query
cursor.execute(create_courseDescription)
cursor.execute(create_courses)
# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()
