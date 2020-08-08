#!/usr/bin/python3
""" Filter states by user input.
    Safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    st_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name=%s \
                ORDER BY cities.id", (st_name,))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
