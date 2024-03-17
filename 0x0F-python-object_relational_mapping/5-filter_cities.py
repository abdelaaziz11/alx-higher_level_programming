#!/usr/bin/python3
'''
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
'''

from sys import argv
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )

    cursor = connection.cursor()
 
    query = "SELECT cities.id, cities.name, states.name\
        FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC"
    """ SELECT cities.name\
            FROM JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s """
    cursor.execute(query, (argv[4],))
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
