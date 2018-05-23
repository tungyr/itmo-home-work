import os
from abc import ABCMeta, abstractmethod

Взаимодействие курсов, учителей и студентов в университете


class Course():  # класс курсов, имеющихся в универе
    __slots__ = ('__coursename', )

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.__coursename = coursename or []

    def add_course(self, coursename):
        if coursename not in self.__coursename:
            self.get_course().append(coursename)

    def get_course(self):
        return self.__coursename

    def remove_course(self, coursename):
        if coursename in self.get_course():
            self.get_course().remove(coursename)



class Men(metaclass=ABCMeta):   # класс люди, объединяющий учителей и студентов
    men_types = {}


class Teacher(Men):      # класс учителей курсов

    def __init__(self, course):
        super().__init__(self, *args, **kwargs)
        self.__coursename = course

    def add_course(self, teacher, course):  # Назначает учителя на курс
        self.__coursename = course

    def get_course(self):
        return self.__coursename

    def remove_course(self, course):
        if course in self.get_course():
            self.get_course().remove(course)


class Student(Men):  # класс студентов

    def __init__(self, course):
        super().__init__(self, *args, **kwargs)
        self.__coursename = course

    def add_cource(self, Student, course):  # Добавляет студента на курс
        self.__coursename = course

    def get_course(self):
        return self.__coursename

    def remove_course(self, course):
        if course in self.get_course():
            self.get_course().remove(course)
