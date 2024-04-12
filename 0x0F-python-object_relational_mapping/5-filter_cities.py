#!/usr/bin/python3
"""
module that takes name of a state as an argument and lists all cities
"""
import sys
import MySQLdb


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
                               db=database)
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    mycursor = mydb.cursor()
    query = "SELECT cities.id, cities.name\
            FROM cities join states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    mycursor.execute(query, (state_name,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    mycursor.close()
    mydb.close()
