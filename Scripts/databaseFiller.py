import pymysql as sql

def fillCourseDatabase(inputList):
    """
    This function takes in a list of inputs and inserts them into the database.
    """
    # Connecting to the database
    connection = sql.connect(host="localhost",user="root",password="Akhil_0506",database="utmCourseDatabase")
    cursor = connection.cursor()
    sqlCommand = "INSERT INTO courses (course_code, title, credit," \
                 "distribution, recommended_prep,prerequisites,exclusions) " \
                 "VALUES (%s, %s, %s,%s,%s,%s,%s) "
    cursor.execute(sqlCommand, tuple(inputList))
    connection.commit()
    cursor.close()
    connection.close()
    return None

def fillonlineReviewsDatabse(inputList):
    """
    This function takes in a list of inputs and inserts them into the database.
    """
    #Connecting to the database
    connection=sql.connect(host="localhost",user="root",password="Akhil_0506",database="utmCourseDatabase")
    cursor=connection.cursor()
    sqlCommand="INSERT INTO onlineReviews (reviewID,sentimentanalysisvalue,reviews,coursecode) VALUES (%s, %s, %s,%s) "
    cursor.execute(sqlCommand,tuple(inputList))
    connection.commit()
    cursor.close()
    connection.close()



