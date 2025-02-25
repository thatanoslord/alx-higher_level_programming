#!/usr/bin/python3
"""  lists all of states from the database of hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cu = db.cusor()
    cu.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cu.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cu.close()
    db.close()
