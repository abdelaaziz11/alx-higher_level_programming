#!/usr/bin/python3
'''
lists all cities from the database hbtn_0e_4_usa
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

    cursor.execute(" SELECT * FROM cities ")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
