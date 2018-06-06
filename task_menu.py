from abc import ABCMeta, abstractmethod


class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class Menu(metaclass=ABCMeta):

    def __init__(self):
        self.commands = {}
        self.index = 0

    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        self.commands[name] = klass

    def execute(self, name, *args, **kwargs):
        klass = self.commands.get(name)
        if klass is None:
            raise CommandException(
                'Command with name "{}" not found!'.format(name)
            )
        comm = klass(name, *args, **kwargs)
        return comm.execute()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(list(self.commands.items())):
            raise StopIteration

        command = list(self.commands.items())[self.index]
        self.index += 1
        return command



class ShowCommand(Command):
    def __init__(self, task_id):
        pass

class ListCommand(Command):
    def __init__(self):
        pass



menu = Menu()
menu.add_command('Show', ShowCommand)
menu.add_command('list', ListCommand)
# menu.add_command('Show Menu', ShowMenuCommand)
menu.execute('show', 1)
menu.execute('list')
menu.execute('unknown')
