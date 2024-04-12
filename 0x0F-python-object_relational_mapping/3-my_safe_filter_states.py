#!/usr/bin/python3
"""
module that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """access to database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    mycursor.execute(query, (state_name,))

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mycursor.close()
    mydb.close()
