#!/usr/bin/python3
"""
module that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        mydb = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cities ORDER BY id ASC")
    mycursor.close()
    mydb.close()
