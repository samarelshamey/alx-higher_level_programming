#!/usr/bin/python3
"""
module that takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """access the database"""
    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    mycursor = mydb.cursor
    mycursor.execute("SELECT * FROM states WHERE \
                     name LIKE BINARY '{}' ORDER BY id ASC".format(argv[4]))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mycursor.close()
    mydb.close()
