class Cell:
    def __init__(self, size):
        self.size = size

    def make_order(self, row):
        return '\n'.join(['*' * row for el in range(self.size // row)]) + '\n' + '*' * (self.size % row)

    def __str__(self):
        return f'Кол-во ячеек в клетке: {self.size}'

    def __add__(self, other):
        return f'Кол-во ячеек в общей клетке: {self.size + other.size}'

    def __sub__(self, other):
        if self.size - other.size > 0:
            return f'Кол-во ячеек в клетке: {self.size - other.size}'
        else:
            return f'Кол-во ячеек в клетке в первой клетке меньше или равно во второй'

    def __mul__(self, other):
        return f'Кол-во ячеек в общей клетке: {self.size * other.size}'

    def __truediv__(self, other):
        return f'Кол-во ячеек в общей клетке: {round(self.size / other.size)}'


cell_1 = Cell(15)
cell_2 = Cell(3)
print(cell_2)
cell = (cell_1 + cell_2)
print(cell)
print(cell_1.make_order(6))