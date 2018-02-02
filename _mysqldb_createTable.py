#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Heroes")
    cur.execute("CREATE TABLE Heroes(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Iron Man')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Capitan America')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Thor')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Viuda Negra')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Hulk')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Bruja Escarlata')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Vision')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Avispa')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Quicksilver')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Ant-Man')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Ojo de Halcon')")       
    
