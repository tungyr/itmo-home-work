import sqlite3

conn = sqlite3.connect('organizer.sqlite')

cursor = conn.cursor()

sql = '''
	CREATE TABLE IF NOT EXISTS orgoniser (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	task_name TEXT NOT NULL DEFAULT,
	task_description TEXT NOT NULL,
	execute_time DATETIME NOT NULL,
	)
'''

cursor.execute(sql)

conn.commit()

conn.close()