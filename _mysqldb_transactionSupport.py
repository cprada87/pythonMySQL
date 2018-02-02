#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


try:
    con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Heroes")
    cur.execute("CREATE TABLE Heroes(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25)) ENGINE=INNODB")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Iron Man')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Capitán América')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Thor')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Viuda Negra')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Hulk')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Bruja Escarlata')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Visión')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Avispa')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Pantera Negra')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Ant-Man')")
    cur.execute("INSERT INTO Heroes(Name) VALUES('Ojo de Halcón')")
    
    con.commit()

    
except mdb.Error, e:
  
    if con:
        con.rollback()
        
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
            
    if con:    
        con.close()
