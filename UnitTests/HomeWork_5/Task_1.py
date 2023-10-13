"""
Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет
 следующие действия:
a. Рассчитывает среднее значение каждого списка.
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.
"""

class NumsLists:
    def __init__(self, lst1: list[int | float], lst2: list[int | float]):
        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self) -> tuple[float, float]:
        avg1 = 0
        if self.lst1:
            avg1 = sum(self.lst1) / len(self.lst1)

        avg2 = 0
        if self.lst2:
            avg2 = sum(self.lst2) / len(self.lst2)

        return avg1, avg2

    def compare_averages(self) -> None:
        avg1, avg2 = self.get_lists_averages()
        if avg1 > avg2:
            print('Первый список имеет большее среднее значение')
        elif avg1 < avg2:
            print('Второй список имеет большее среднее значение')
        else:
            print('Средние значения равны')