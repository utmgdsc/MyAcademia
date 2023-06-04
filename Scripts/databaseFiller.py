import pymysql as sql


def fillCourseDatabase(inputList):
    """
    This function takes in a list of inputs and inserts them into the database.
    """
    # Connecting to the database
    connection = sql.connect(host="localhost",user="root",password="utm@GDSC",database="testDatabase")
    cursor = connection.cursor()
    sqlCommand = "INSERT INTO courses (course_code, title, credit," \
                 "distribution, recommended_prep,prerequisites,exclusions) " \
                 "VALUES (%s, %s, %s,%s,%s,%s,%s) "
    cursor.execute(sqlCommand, tuple(inputList))
    connection.commit()
    cursor.close()
    connection.close()

    return None


