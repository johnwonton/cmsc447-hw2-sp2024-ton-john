import sqlite3 as sql

#Connect to SQLite
con = sql.connect('databaseHW2.db')

#Create a connection
cur = con.cursor()

#If it already exists, then drop the "students" table.
cur.execute("DROP TABLE IF EXISTS students")

#Then, create the "students" table in the databaseHW2 database.
sql ='''CREATE TABLE "students" ( "Name" TEXT, "Id" INTEGER, "Points" INTEGER)'''
cur.execute(sql)

#Commit the changes then close the connection.
con.commit()
con.close()