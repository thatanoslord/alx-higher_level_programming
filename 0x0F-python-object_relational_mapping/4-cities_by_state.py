#!/usr/bin/python3
"""  lists all of states from Database of hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = db.cusor()
    cu.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
