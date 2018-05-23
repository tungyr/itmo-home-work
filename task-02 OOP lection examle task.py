from abc import ABCMeta, abstractmethod
import os


class ParamHandler(metaclass=ABCMeta):
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
def get_instance(source):
    _, ext = os.path.splitext(str(source).lower())
    if ext == '.xml':
        return XmlParamHandler(source)
        return TextParamHandler(source)


class TextParamHandler(ParamHandler):
            def __init__(self, source):
                self.source = source
                self.params = {}

            def read(self):
                with open(self.source) as f:
                    result = f.read()

            def write(self):
                with open(self.source, 'w') as f:
                    result = f.write(self.params, f)


class JsonParamHandler(ParamHandler):
            def __init__(self, source):
                self.source = source
                self.params = {}

            def read(self):
                with open(self.source) as f:
                    result = json.load(f)

            def write(self):
                with open(self.source, 'w') as f:
                    result = json.dump(self.params, f)


class PickleParamHandler(ParamHandler):
            def __init__(self, source):
                self.source = source
                self.params = {}

            def read(self):
                with open(self.source) as f:
                    result = pickle.load(f)

            def write(self):
                with open(self.source, 'w') as f:
                    result = pickle.dump(self.params, f)


class ParamHandlerException(Exception):
    def __init__(self, text):
        self.text = text


class ParamHandler(metaclass=ABCMeta):
    types = {}

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
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )
            return klass(source, *args, **kwargs)


config = ParamHandler.get_instance('./params.txt')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()  # запись файла в XML формате

config = ParamHandler.get_instance('./params.txt')
config.read()  # читаем данные из текстового файла


ParamHandler.add_type('txt', TextParamHandler)

ParamHandler.add_type('xml', XmlParamHandler)

ParamHandler.add_type('json', JsonParamhandler)

Paramhandler.add_type('pickle', PickleParamHandler)


config = ParamHandler.get_instance('./params.xml')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()  # запись файла в XML формате
config = ParamHandler.get_instance('./params.txt')
config.read()


config = ParamHandler.get_instance('./params.pickle')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()


config = ParamHandler.get_instance('./params.json')
config.add_param('key1', 'val1')
config.add_param('key2', 'val2')
config.add_param('key3', 'val3')
config.write()
