#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Heroes LIMIT 11")

    rows = cur.fetchall()

    desc = cur.description

    print "%s %3s" % (desc[0][0], desc[1][0])

    for row in rows:    
        print "%2s %3s" % row
