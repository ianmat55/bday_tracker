import sqlite3

connection = sqlite3.connect('database.db')
c = connection.cursor()

with open('schema.sql') as f:
	c.executescript(f.read())

connection.commit()
connection.close()
