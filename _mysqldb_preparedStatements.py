#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')    
with con:    

    cur = con.cursor()
        
    cur.execute("UPDATE Heroes SET Name = %s WHERE Id = %s", 
        ("Pantera Negra", "9"))        
    
    print "Number of rows updated:",  cur.rowcount
