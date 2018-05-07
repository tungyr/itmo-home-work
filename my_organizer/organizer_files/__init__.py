import sys

from organizer_files import storage

get_connection = lambda: storage.connect('organizer.sqlite')


def action_add():
    """Добавить задачу"""
    task = input ('\nВведите задачу: ')
    status = ('undone')
    with get_connection() as conn:
        task = storage.add_task(conn, task, status)


def action_find_all():
    """Вывести все задачи"""
    with get_connection() as conn:
        print (storage.find_all(conn))


def action_edit():
    rev_task_id = input ('\nTask ID for revise?: ')
    rev_task = input ('\nRevise task: ')
    with get_connection() as conn:
        storage.task_edit(conn, rev_task_id, rev_task)



def action_complete():
    """Завершить задачу"""
    compl_task_id = input ('\nTask ID for complete?: ')
    status = 'done'
    with get_connection() as conn:
        storage.task_compl(conn, compl_task_id, status)


def action_again():
    """Начать задачу сначала"""

def action_show_menu():
    """Показать меню"""

    print('''
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
m. Показать меню
q. Выйти
''')

def action_exit():
    """Выйти"""
    sys.exit(0)      # завершает с 0-вым кодом - все хорошо


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_find_all,
        '2': action_add,
        '3': action_edit,
        '4': action_complete,
        '5': action_again,
        'm': action_show_menu,
        'q': action_exit,
        }


    while 1:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
