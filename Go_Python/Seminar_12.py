"""
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
недопустимы.Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов
вместе взятых.
"""

import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not all(map(lambda val: val.istitle(), value.split(' '))):
            raise ValueError(f"ФИО только с заглавной буквы!")
        instance.__dict__[self.name] = value


class Student:
    name = NameValidator()

    def __init__(self, name):
        self.name = name
        self.subject_grades = {}
        self.subject_tests = {}

        with open('Go_Python\Seminar_12\subjects.csv', 'r') as csv_file:
            subjects = csv.reader(csv_file, delimiter="\n")
            for item in subjects:
                self.subject_grades[item[0]] = []
                self.subject_tests[item[0]] = []

    def add_score(self, score, subject):
        if score < 2 or score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subject_grades[subject].append(score)

    def add_test_result(self, result, subject):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.subject_tests[subject].append(result)

    def average_score_student(self):
        subject_scores = [sum(score) for score in self.subject_grades.values() if score != []]
        if not subject_scores:
            return 0
        return sum(subject_scores) / len(subject_scores)

    def subject_test_average(self, subject):
        return subject, sum(self.subject_tests[subject]) / len(self.subject_tests[subject])


# Создание экземпляра класса Student
student = Student("Наталья Ивановна Петина")

# Добавление оценок и результатов тестов
student.add_score(4, 'Математика')
student.add_score(5, 'Математика')
student.add_score(4, 'Русский язык')

student.add_test_result(78, 'Математика')
student.add_test_result(80, 'Русский язык')
student.add_test_result(60, 'Русский язык')

# Расчет среднего балла по всем предметам
print("Средний балл студента", student.average_score_student())

# Расчет среднего балла по тестам определенного предмета
print("Средний балл по тесту:", student.subject_test_average('Русский язык'))


"""
import csv
from functools import reduce
from pathlib import Path


class Validate:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    @staticmethod
    def validate(value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть текстом')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _lessons = None

    def __init__(self, name: str, second_name: str, surname: str, lessons: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.lessons = lessons

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, less: Path):
        if self.lessons is not None:
            raise AttributeError(f'Список предметов уже определён')
        self._lessons = {"lessons": {}}
        with open(less, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"estimates": [],
                                                    "tests": [],
                                                    "middle_estimate_test": None}
        self._lessons["middle_estimate"] = None

    def new_estimate(self, name_of_lesson: str, number: int, type_est: str = "less"):
        if name_of_lesson not in self.lessons["lessons"].keys():
            raise AttributeError("Предмет не изучается")
        if type_est == "less":
            if number < 2 or number > 5:
                raise ValueError("Оценка вне допустимого диапазона (2-5)")
            self.lessons["lessons"][name_of_lesson]["estimates"].append(number)
            self.lessons["middle_estimate"] = self.middle_estimate(self.lessons)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Оценка вне допустимого диапазона (0-100)")
            self.lessons["lessons"][name_of_lesson]["tests"].append(number)
            self.lessons["lessons"][name_of_lesson]["middle_estimate_test"] = \
                reduce(lambda x, y: x + y, self.lessons["lessons"][name_of_lesson]["tests"]) / \
                len(self.lessons["lessons"][name_of_lesson]["tests"])

    @staticmethod
    def middle_estimate(lessons: dict):
        all_estimates = []
        [all_estimates.extend(lessons["lessons"][name]["estimates"]) for name in lessons["lessons"]]
        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'''Средние баллы студента: 
        полное имя = "{self.name} {self.second_name} {self.surname}",
        средний балл = {self.lessons["middle_estimate"]}\n'''
        for key, value in self.lessons["lessons"].items():
            result += f' средний балл по тестам {key} =  {value["middle_estimate_test"]}\n'

        return result


if __name__ == '__main__':
    info = Student(, Path('subjects.csv'))
    info.new_estimate("русский язык", 3)
    info.new_estimate("русский язык", 5)
    info.new_estimate("математика", 4)
    info.new_estimate("информатика", 4)
    info.new_estimate("математика", 5)
    info.new_estimate("русский язык", 5)
    info.new_estimate("информатика", 3)
    info.new_estimate("математика", 5)
    info.new_estimate("русский язык", 3)
    info.new_estimate("математика", 4)
    info.new_estimate("математика", 68, "test")
    info.new_estimate("математика", 99, "test")
    info.new_estimate("русский язык", 29, "test")
    info.new_estimate("русский язык", 100, "test")
    info.new_estimate("русский язык", 18, "test")
    info.new_estimate("информатика", 74, "test")
    info.new_estimate("информатика", 39, "test")

    print(info)
"""