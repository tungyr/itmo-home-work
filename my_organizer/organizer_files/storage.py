import os.path as Path
import sqlite3

SQL_INSERT_TASK = 'INSERT INTO organizer (task, status) VALUES (?,?)'
SQL_UPDATE_TASK = '''
    UPDATE organizer SET task=?, status=? WHERE id=?
'''

SQL_SELECT_ALL ='''
    SELECT
        id, task, status, created
    FROM
        organizer
        '''

SQL_SELECT_TASK = SQL_SELECT_ALL + ' WHERE task=?'
SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_EDIT_TASK = '''
    UPDATE organizer SET task=? WHERE id=?
'''

SQL_COMPL_TASK = '''
    UPDATE organizer SET task=? WHERE id=?
'''


#def connect (db_name=':memory:'):
def connect(db_name=None):
    """Выполняет подключение к БД"""
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn


def initialize(conn):
    script_path = Path.join(Path.dirname(__file__), 'schema.sql')


    with conn, open(script_path) as f:
        conn.executescript(f.read())

def task_edit(conn, rev_task, rev_task_id):
    with conn:
        cursor = conn.execute(SQL_EDIT_TASK, (rev_task, rev_task_id))


def task_compl(conn, coml_task_id, status):
    with conn:
        cursor = conn.execute(SQL_COMPL_TASK, (coml_task_id, status))


def add_task(conn, task, status):
    """Добавляет задачу в БД"""

    if not task:
        raise RuntimeError("Task can't be empty.")

    with conn:
        found = find_task(conn, task)

        if found:
            print('\nTask alrealy exist!')

        cursor = conn.execute(SQL_INSERT_TASK, (task,status))

        pk = cursor.lastrowid

        conn.execute(SQL_UPDATE_TASK, (task, status, pk))

        return task

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_task(conn, task):
    """Возвращает task"""

    with conn:
        cursor = conn.execute(SQL_SELECT_TASK, (task,))
        return cursor.fetchone()
