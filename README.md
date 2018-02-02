#  MySQL Python tutorial

This is MySQL Python programming tutorial with the MySQLdb module.
The examples were created and tested on ArchLinux.

## PROGRAMS:

* Ver. Python = 2.0
* Ver. DataBase = 10.1.30-MariaDB
* Editor = Vim

## INSTRUCTIONS:

1. Insert following sentences on mariadb/mysql:
    * mysql -u root -p
    * CREATE DATABASE vengadores;
    * CREATE USER 'nickFury'@'localhost' IDENTIFIED BY 'shield';
    * USE vengadores;
    * GRANT ALL ON vengadores.* TO 'nickFury'@'localhost';
    * quit;
2. run: "_mysql_dbmodule.py"
3. run: "_mysqldb_createTable.py"
4. run: "_mysqldb_retrievingData.py"
5. run: "_mysqldb_retrievingData2.py"
6. run: "_mysqldb_dictionaryCursor.py"
7. run: "_mysqldb_columHeaders.py"
8. run: "_mysqldb_preparedStatments.py"
9. Insert sentence on mariadb:
    * CREATE TABLE Images (Id INT PRIMARY KEY, Data LONGBLOB);
    * NOTE: You need a image for next sample named "viuda.jpg" stored on your script directory (max=1MB)
10. run: "_mysqldb_insertingImages.py"
11. run: "_mysqldb_readingImages.py"
12. run: "_mysqldb_transactionSupport.py"


