from abc import ABCMeta, abstractmethod
import re


class ValidatorException(Exception):
        pass


class Validator(metaclass=ABCMeta):
    types = {}

    def __init__(self, value):
        self.source = value

    @abstractmethod
    def validate(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException('Type must have a name!')

        if not issubclass(klass, Validator):
            raise ValidatorException(
                'Class "{}" is not Validator!'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, name):
        klass = cls.types.get(name)
        if klass is None:
            raise ValidatorException(
                'Type "{}" not found!'.format(name)
            )
        return klass(name)


class EMailValidator(Validator):
            """
            Валидация email адреса
            """
            def validate(self, email):
                if "@" in email:
                    True
                    print("True")
                else:
                    False
                    print("False")


class DateTimeValidator(Validator):
            """
            Валидация формата даты и времени
            """
            def validate(self, datetime):
                pattern = (r'\d{,4}[-./]\d{,2}[-./]\d{,4}[ ]?\d{2}?[:]?\d[00]?[:]?\d[00]?')
                res = re.findall(pattern, datetime)
                res = ''.join(res)

                if datetime == res:
                    return True
                else:
                    return False


Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)

validator = Validator.get_instance('datetime')
validator.validate('1/9/2017 12:00:00')
