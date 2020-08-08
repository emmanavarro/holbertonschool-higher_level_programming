#!/usr/bin/python3
""" Lists all all_states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv


if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY 'N%' ORDER BY id ASC")
    all_states = cur.fetchall()
    for states in all_states:
        print(states)
    cur.close()
    db.close()
