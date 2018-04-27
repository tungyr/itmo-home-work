print("""
1. Выести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выйти
		""")

        
def organiser(usr_inp):
    s = 1
    while s == 1:
        if usr_inp == 1:
            print ("Вывожу все Ваши задачи")
            import organizer.all_tsk         # импорт из модуля функции вывода списка задач (или напрямую из БД?)
        elif usr_inp == 2:
            print ("Создание новой задачи")
            import organizer.new_tsk         # новая задача
        elif usr_inp == 3:
            print ("Редактирование задачи")
            import organizer.edit_tsk        # редактировать задачу
        elif usr_inp == 4:
            print ("Завершение задачи")
            import organizer.complete_tsk    # завершить задачу
        elif usr_inp == 5:
            print ("Начинаем задачу сначала")
            import organizer.repeat_tsk      # начать задачу снова
        elif usr_inp == 6:
            print ("До встречи!")
            print("""
                1. Выести список задач
                2. Добавить задачу
                3. Отредактировать задачу
                4. Завершить задачу
                5. Начать задачу сначала
                6. Выйти
                        """)
        
orginiser(int(input("Введите номер пункта меню: "))

try:
    i = int(input())
    # print(i[0])
except ValueError:
    print('Не корректное число!')

    
def all_tsk(date=current_date)

def new_tsk(name)

def edit_tsk(id,name)

def complete_tsk(tsk_done)

def repeat_tsk(tsk_repeat)