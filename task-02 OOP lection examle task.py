from abc import ABCMeta, abstractmethod
import os
import pickle
import json


class ParamHandlerException(Exception):
        pass


class ParamHandler(metaclass=ABCMeta):
    types = {}

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        print('ext:', ext)
        klass = cls.types.get(ext)
        print('klass:', klass)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )
        return klass(source, *args, **kwargs)


class TextParamHandler(ParamHandler):
            """
            Чтение txt файла и присвоение параметров self.params
            """
            def read(self):
                with open(self.source) as f:
                    self.params = f.read()

            def write(self):
                """
                Запись параметров self.params в txt файл
                """
                with open(self.source, 'w') as f:
                    print('self.params:', self.params, type(self.params))
                    # self.params = str(self.params)
                    print('self.params:', self.params, type(self.params))
                    for key, value in self.params.items():
                        param = key + ':' + value + '\n'
                        f.write(param)


class JsonParamHandler(ParamHandler):

            def read(self):
                """
                Чтение json файла и присвоение параметров self.params
                """
                with open(self.source) as f:
                    json_params = json.load(f)
                    for i in json_params:
                        self.params[i] = json_params[i]

            def write(self):
                """
                Запись параметров self.params в json файл
                """
                with open(self.source, 'w') as f:
                    json.dump(self.params, f, indent=4)


class PickleParamHandler(ParamHandler):

            def read(self):
                """
                Чтение pickle файла и присвоение параметров self.params
                """
                with open(self.source, 'rb') as f:
                    pickle_params = pickle.load(f)
                    for i in pickle_params:
                        self.params[i] = pickle_params[i]

            def write(self):
                """
                Запись параметров self.params в pickle файл
                """
                with open(self.source, 'wb') as f:
                    pickle.dump(self.params, f)


ParamHandler.add_type('txt', TextParamHandler)
ParamHandler.add_type('json', JsonParamHandler)
ParamHandler.add_type('pickle', PickleParamHandler)

config = ParamHandler.get_instance('./params.pickle')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()

config = ParamHandler.get_instance('./params.json')
config.read()
