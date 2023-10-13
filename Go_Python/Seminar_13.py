"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
 Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""

class MatrixExeption(Exception):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f'Ошибка в размерности матриц, matrix_a = {self.x1}x{self.y1}; matrix_b = {self.x2}x{self.y2}'


class Matrix():
    """Класс для создания матриц и операциями сложения и перемножения между ними"""

    def __init__(self, matrix: list):
        self._matrix = matrix

    def __eq__(self, __other: object) -> bool:
        """Cравнение двух матриц между собой"""

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
        """Сложение матриц одинаковой размерности"""

        if len(self._matrix) != len(other._matrix):
            raise MatrixExeption(len(self._matrix), len(self._matrix[0]), len(other._matrix), len(other._matrix[0]))
        else:
            __result_matrix = []
            for i in range(len(self._matrix)):
                line1 = self._matrix[i]
                line2 = other._matrix[i]
                c = [x + y for x, y in zip(line1, line2)]
                __result_matrix.append(c)
            return Matrix(__result_matrix)

    def __mul__(self, other):
        """Перемножение двух матриц"""

        if len(self._matrix[0]) != len(other._matrix):
            raise MatrixExeption(len(self._matrix), len(self._matrix[0]), len(other._matrix), len(other._matrix[0]))
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
    matrix_2 = Matrix([[12, 2, 3], [6, 5, 6], [7, 7, 9]])
    matrix_3 = Matrix([[9, 2, 3], [20, 5, 6], [4, 8, 16]])
    matrix_4 = Matrix([[11, 2, 3], [4, 50, 6]])

    # Cравнение матриц
    # print(matrix_1 == matrix_2)
    # print(matrix_1 == matrix_2)

    # Сложение матриц
    # print(matrix_1 + matrix_3)
    # print(matrix_1 + matrix_4)

    # Умножение матриц
    # print(matrix_1 * matrix_3)
    # print(matrix_1 * matrix_4)