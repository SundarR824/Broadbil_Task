import mysql.connector


def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sundar123',
            # database='school'
        )
        print("Connected to the database.")
        cur = connection.cursor()
        query = "create database school;"
        cur.execute(query)
        connection.commit()
        connection.close()
        # res = cur.fetchall()
        # print(res)

    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)


connect()
