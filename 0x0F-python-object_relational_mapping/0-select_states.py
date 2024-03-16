#!/usr/bin/python3
import sys
import MySQLdb

def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db=database_name, port=3306)
    cursor = connection.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
