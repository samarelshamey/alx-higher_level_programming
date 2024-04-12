#!/usr/bin/python3
"""
module that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        mydb = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database
                               sname=state_name)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)
    mycusrsor = mydb.cursor
    mycursor.execute("SELECT * FROM states WHERE name=sname ORDER BY id ASC")
    myresutl = mycursor.fetchall()
    for x in myresult:
        print(x)
    mycursor.close()
    mydb.close()
