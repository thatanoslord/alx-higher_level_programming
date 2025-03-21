#!/usr/bin/python3
"""  lists all of states from  Database of hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = db.cursor()
    cu.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
