#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
from 0-select_states import states
import MySQLdb

con = MySQLdb.connect(host = "localhost", user = "mysql username", passwd = "mysql password", database = "database name")
sql = "SELECT * FROM states"
for name in sql:
    print(states.id, states.name)
