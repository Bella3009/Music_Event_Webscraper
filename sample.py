import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM Events WHERE Band='Lions'")
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("SELECT Band,Date FROM Events WHERE Band='Lions'")
rows = cursor.fetchall()
print(rows)

# New rows
new_rows = [('Cats', 'Cat City', '2088.10.15'),
            ('Tigers', 'Tiger City', '2088.10.15')]

cursor.executemany("INSERT INTO Events VALUES(?,?,?)", new_rows)
connection.commit()