#!/usr/bin/python3
"""module that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

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
        sys.exit(1)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states
                     WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    mycursor.close()
    mydb.close()
