#!/usr/bin/python3
"""
module that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """access to database"""
    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    mycursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    mycursor.execute(query, (state_name,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
