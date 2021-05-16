class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        answer = []
        if len(self.matrix) == len(other.matrix):
            for row_1, row_2 in zip(self.matrix, other.matrix):
                if len(row_1) != len(row_2):
                    return f'Сложение не возможно, размеры матриц не соответствуют'
                else:
                    row = [el_1 + el_2 for el_1, el_2 in zip(row_1, row_2)]
                    answer.append(row)
            return '\n'.join([' '.join(map(str, row)) for row in answer])
        else:
            return f'Сложение не возможно, размеры матриц не соответствуют'


matrix_1 = Matrix([[5, 6, 3], [10, 15, 3], [1, 9, 7]])
matrix_2 = Matrix([[-1, 6, 5], [5, 5, 8], [-2, 12, 7]])
matrix_3 = matrix_1 + matrix_2

print(matrix_3)
