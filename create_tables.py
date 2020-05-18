import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

#must be integer
#This is the only place where int vs INTEGER matters-in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table) #executes the table

cursor.execute("INSERT INTO items VALUES ('hello', 123456789)")

connection.commit()

connection.close()
