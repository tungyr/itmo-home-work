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
SQL_SELECT_TASK_BY_STATUS = SQL_SELECT_ALL + ' WHERE status=?'

SQL_EDIT_TASK = '''
    UPDATE organizer SET task=? WHERE id=?
'''

SQL_COMPL_TASK = '''
    UPDATE organizer SET status=? WHERE id=?
'''

SQL_DELETE_TASK = '''DELETE FROM organizer WHERE id=?'''

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
        cursor = conn.execute(SQL_EDIT_TASK,(rev_task, rev_task_id))
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (rev_task_id,)) #выборка последней измененной задачи для демонстрирования результата
        return cursor.fetchone()

def task_compl(conn, status, compl_task_id):
    with conn:
        cursor = conn.execute(SQL_COMPL_TASK,(status, compl_task_id))
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (compl_task_id,))
        return cursor.fetchone()


def task_repeat(conn, status, repeat_task_id):
    with conn:
        cursor = conn.execute(SQL_COMPL_TASK,(status, repeat_task_id))
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (repeat_task_id,))
        return cursor.fetchone()

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
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
        return task, cursor.fetchone()

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        rows = cursor.fetchall()
        print ("\nСписок всех задач: ")
        for row in rows:                        # представление списка задач в столбик
            print(row)

def find_status(conn, status_find):
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_STATUS,(status_find,))
        rows = cursor.fetchall()
        print ("\nСписок запрошенных задач: ")
        for row in rows:
            print(row)

def task_delete(conn,delete_task_id):
    with conn:
        found = find_task_pk(conn, delete_task_id)

        if found:
            with conn:
                cursor = conn.execute(SQL_DELETE_TASK,(delete_task_id))
                print('Задача удалена!')
                find_all(conn)
        else:
                print('\nНет такой задачи!')

def find_task(conn, task):
    """Возвращает task"""

    with conn:
        cursor = conn.execute(SQL_SELECT_TASK, (task,))
        return cursor.fetchone()

def find_task_pk(conn, id):
    """Возвращает task по ID"""
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (id,))
        return cursor.fetchone()
