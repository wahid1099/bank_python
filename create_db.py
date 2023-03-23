import pymysql

conn = pymysql.connect(
    host="localhost",
    user="wahid",
    passwd="Wahid@#81"
)

mycursor = conn.cursor()

sql_command = """
                    CREATE DATABASE bank;
                """

mycursor.execute(sql_command)
