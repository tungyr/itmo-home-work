from abc import ABCMeta, abstractmethod


class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class Menu():

    commands = {}

    def __init__(self, *args, **kwargs):
        pass

    def __iter__(self):
        return self

    def __next__(self):
            for i in dict.items(self.commands):
                print(i)
            else:
                raise StopIteration

    @classmethod
    def add_command(cls, name, klass):
            if not name:
                raise CommandException('Command must have a name!')
            if not issubclass(klass, Command):
                raise CommandException(
                    'Class "{}" is not Command!'.format(klass)
                )
            cls.commands[name] = klass

    @classmethod
    def execute(cls, name, *args, **kwargs):
        klass = cls.commands.get(name)
        if klass is None:
            raise CommandException(
                'Command with name "{}" not found!'.format(name)
            )
        comm = klass(name, *args, **kwargs)
        comm.execute()


class ShowAllCommand(Command):
    def __init__(self, name, *args, **kwargs):
        pass

    def execute(self):
        print('Show all command performed!')


class AddTaskCommand(Command):
    def __init__(self, name, *args, **kwargs):
        pass

    def execute(self):
        print('Add task command performed!')


class ShowMenuCommand(Command):
    def __init__(self, name, *args, **kwargs):
        pass

    def execute(self):
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

# Menu.add_command('Show All Commands', ShowAllCommand)
# Menu.add_command('Add Task', AddTaskCommand)
# Menu.add_command('Show Menu', ShowMenuCommand)
# Menu.execute('Show All Commands')
# Menu.execute('Add Task')
# Menu.execute('Show Menu')
# menu.execute('unknown')

# lst = Menu('')
# for name, command in lst:
    # print(name, command)
