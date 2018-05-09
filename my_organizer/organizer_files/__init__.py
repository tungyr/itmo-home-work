import sys

from organizer_files import storage

get_connection = lambda: storage.connect('organizer.sqlite')


def action_add():
    """Добавить задачу"""
    task = input ('\nВведите новую задачу: ')
    status = ('undone')
    with get_connection() as conn:
        task = storage.add_task(conn, task, status)
    print('\nЗадача добавлена: ', task)



def action_find_all():
    """Вывести все задачи"""
    with get_connection() as conn:
        storage.find_all(conn)



def action_find():
    """Вывести задачи по параметрам"""

    print('''
    1. Вывести все задачи
    2. Вывести завершенные задачи
    3. Вывести незавершенные задачи
    4. Вывести задачи на повторе
    q. Выход в предыдущее меню
    ''')

    actions_find = {
        '1': action_find_all,       # ключ словаря - параметр, по которому выбираются задачи в БД
        '2': 'done',
        '3': 'undone',
        '4': 'repeat',
        'q': main,
        }

    while 1:
        cmd = input('\nВведите номер пункта: ')
        action = actions_find.get(cmd)

        if action == action_find_all or action == main:     # проверка выбора пользователем показа меню или показа всех задач без разбора
            action()
        elif action:
            status_find = action
            with get_connection() as conn:
                storage.find_status(conn, status_find)
        else:
            print('Неизвестная команда')



def action_edit():
    rev_task_id = input ('\nID задачи для редактирования: ')
    rev_task = input ('\nНовый текст задачи: ')
    with get_connection() as conn:
        storage.task_edit(conn, rev_task, rev_task_id)
    print('\nЗадача изменена: ', storage.task_edit(conn, rev_task, rev_task_id)) # Демонстрирование результата в подтверждение выполнения действия

def action_complete():
    """Завершить задачу"""
    compl_task_id = input ('\nID завершенной задачи: ')
    status = ('done')
    with get_connection() as conn:
        storage.task_compl(conn, status, compl_task_id)
    print('\nЗадача завершена: ', storage.task_compl(conn, status, compl_task_id))

def action_again():
    """Начать задачу сначала"""
    repeat_task_id = input ('\nID задачи на повторение: ')
    status = ('repeat')
    with get_connection() as conn:
        storage.task_repeat(conn, status, repeat_task_id)
    print('\nЗадача изменена: ', storage.task_repeat(conn, status, repeat_task_id))

def action_delete():
    """Удаление задачи"""
    delete_task_id = input ('\nID задачи для удаления: ')
    with get_connection() as conn:
        storage.task_delete(conn,delete_task_id)
        



def action_show_menu():
    """Показать меню"""

    print('''
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Удалить задачу
m. Показать меню
q. Выйти
''')

def action_exit():
    """Выйти"""
    print("\nДо новых встреч!")
    sys.exit(0)      # завершает с 0-вым кодом - все хорошо


def main():
    with get_connection() as conn:
        storage.initialize(conn)

    action_show_menu()

    actions = {
        '1': action_find,
        '2': action_add,
        '3': action_edit,
        '4': action_complete,
        '5': action_again,
        '6': action_delete,
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
