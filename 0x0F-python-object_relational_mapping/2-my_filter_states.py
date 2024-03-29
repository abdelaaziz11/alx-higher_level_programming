#!/usr/bin/python3
'''
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
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

    cursor.execute(" SELECT * FROM states\
            WHERE BINARY name = '{}' ".format(argv[4]))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
