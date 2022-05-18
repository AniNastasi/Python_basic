# 1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self): ## сперва я вывела матрицу данным способом. Но позже, когда я начала суммировать 2 матрицы,
        mx = ''        ## у меня выходила ошибка, что 'int' объект не итерабельный. Я Пыталась поменять типы данных,
        for row in self.matrix: ## но у меня не выводилась матрица. Далее (ниже строки 14 и 15) я нашла в интернете
            mx1 = ''            ## другой способ решения, но с ним я получала такую же ошибку. Не могу понять что нужно поменять
            for col in str(row):
                mx1 += col + ''
            mx += mx1 + '\n'
        return mx
    # def __str__(self):
    #     return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        # sum =
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                return Matrix(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(self.matrix[i][j] + other.matrix[i][j])

a = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
b = Matrix([[1, 1, 1], [4, 8, 16], [9, 27, 81]])
print(a)
print(b)
print(a + b)

# 2
class Textil:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_usage_c(self):
        return self.size / 6.5 + 0.5

    def get_usage_s(self):
        return self.height * 2 + 0.3

    @property
    def get_totalusage(self):
        return str(f'Total textile consumption is: \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)} sqm')


class Coat(Textil):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.usage_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'The textile consumption for the coat is: {self.usage_c} sqm'


class Suit(Textil):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.usage_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'The textile consumption for the suit is: {self.usage_s} sqm'

coat = Coat(42, 1.75)
suit = Suit(48, 1.90)
print(coat)
print(suit)
print(coat.get_totalusage)
print(suit.get_totalusage)
print(coat.get_usage_c())
print(suit.get_usage_s())

# 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
       if (self.quantity - other.quantity) > 0:
           return self.quantity - other.quantity
       else:
           print('Negative value')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

c1 = Cell(47)
c2 = Cell(5)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 / c2)
print(c1.make_order(5))
print(c2.make_order(6))
