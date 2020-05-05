import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

users = [(1, 'mahendra', '09876'), (2, 'iyer', 'asdf'), (3, 'kobhar', 'lkjh'), (4, 'umu', 'poiu'), (5, 'vind', 'qwert')]
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)

connection.commit()
connection.close()
