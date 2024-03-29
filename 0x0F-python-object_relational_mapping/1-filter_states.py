#!/usr/bin/python3
'''
lists all states with a name starting with N
from the database hbtn_0e_0_usa
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

    cursor.execute(" SELECT * FROM states")
    """ cursor.execute(" SELECT MIN(id), name FROM states WHERE name\
            LIKE 'N%' GROUP BY name") """

    results = cursor.fetchall()

    for row in results:
        if row[1].startswith("N"):
            print(row)

    cursor.close()
    connection.close()
