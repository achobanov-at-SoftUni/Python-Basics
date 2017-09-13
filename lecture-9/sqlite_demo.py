import sqlite3

CONNECTION = sqlite3.connect('data/sales-example.db')

cursor = CONNECTION.cursor()
cursor.execute('select * from catalog')
results = cursor.fetchall()
print(results)