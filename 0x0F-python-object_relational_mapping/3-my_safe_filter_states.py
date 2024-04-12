#!/usr/bin/python3
"""
module that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        mydb = MySQLdb.connect(hotsname="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(state_name)s
                         ORDER BY id ASC", {'state_name: sys.argv[4]'})
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        mycursor.close()
        mydb.close()
