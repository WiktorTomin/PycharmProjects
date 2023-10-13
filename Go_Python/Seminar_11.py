"""
Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц
"""

from random import randint as rand

class Matrix():

    def __init__(self, matrix: list):
        self._matrix = matrix

    def __eq__(self, __other: object) -> bool:

        if len(self._matrix) != len(__other._matrix):
            return False
        else:
            __flag = False
            for i in range(len(self._matrix)):
                if self._matrix[i] == __other._matrix[i]:
                    __flag = True
                else:
                    self._flag = False
            return __flag

    def __add__(self, other):

        if len(self._matrix) != len(other._matrix):
            raise ArithmeticError('Ошибка:сложение матриц разного размера не поддерживается!')
        else:
            __result_matrix = []
            for i in range(len(self._matrix)):
                line1 = self._matrix[i]
                line2 = other._matrix[i]
                c = [x + y for x, y in zip(line1, line2)]
                __result_matrix.append(c)
            return Matrix(__result_matrix)

    def __mul__(self, other):

        if len(self._matrix[0]) != len(other._matrix):
            raise ArithmeticError('Ошибка:умножение матриц разного размера не поддерживается!')
        else:
            result = []
            for i in range(len(self._matrix)):
                new_row = []
                for j in range(len(other._matrix[0])):
                    elem = 0
                    for k in range(len(other._matrix)):
                        elem += self._matrix[i][k] * other._matrix[k][j]
                    new_row.append(elem)
                result.append(new_row)
            return Matrix(result)

    def __str__(self) -> str:
        result_string = ''

        for i in self._matrix:
            result_string += f'{i}\n'

        return result_string


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    matrix_3 = Matrix([[4, 2, 3], [13, 5, 6], [72, 8, 90]])
    matrix_4 = Matrix([[6, 2, 3], [34, 5, 6]])

#Cравнение матриц
 #print(matrix_1 == matrix_2)
 #print(matrix_1 == matrix_2)

# Сложение матриц
 #print(matrix_1 + matrix_3)
 #print(matrix_1 + matrix_4)

# Умножение матриц
 #print(matrix_1 * matrix_3)
#print(matrix_1 * matrix_4)
