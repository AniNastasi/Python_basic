# 1
class Data:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = dd_mm_yy

    @classmethod
    def get_date(cls, dd_mm_yy):
        my_date = []

        for i in dd_mm_yy.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return f'All right'
                else:
                    return f'Error! Check up the year!'
            else:
                return f'Error! Check up the month!'
        else:
            return f'Error! Check up the day!'

    def __str__(self):
        return f'Today is {Data.get_date(self.dd_mm_yy)}'


today = Data('12 - 5 - 2022')
print(today)
print(Data.valid(110, 5, 2022))
print(Data.get_date('10 - 5 - 2022'))

# 2
class ZeroDivision:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
        print(ZeroDivision.divide_by_zero(dividend, divisor))

    def __str__(self):
        return f'The result of division of {self.dividend} by {self.divisor}'

    @staticmethod
    def divide_by_zero(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return (f'Zero Division Error')

a = ZeroDivision(13, 0)
print(a)

# 3
class TypeErr(Exception):
    def __init__(self, txt):
        self.txt = txt
ls = []
while True:
    try:
        el = input('Enter a number to the list: ')
        if el == 'no':
            print('end!')
            break
        if not el.isdigit():
            raise TypeErr('Not a number!')
    except TypeErr as err:
        print(err)
    else:
        print(el)

        a = ls.append(int(el))
print(ls)

# 4
class Store:

    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

class Printer(Store):
    def __init__(self, name, brand, price, quantity, operation):
        super().__init__(name, brand, price, quantity)
        self.operation = operation

    def __str__(self):
        return f'Name: {self.name}\nBrand: {self.brand}\nPrice: {self.price}\nQuantity: {self.quantity}\nOperation: {self.operation}'


class Scanner(Store):
    def __init__(self, name, brand, price, quantity, operation):
        super().__init__(name, brand, price, quantity)
        self.operation = operation

    def __str__(self):
        return f'Name: {self.name}\nBrand: {self.brand}\nPrice: {self.price}\nQuantity: {self.quantity}\nOperation: {self.operation}'


class Copier(Store):
    def __init__(self, name, brand, price, quantity, operation):
        super().__init__(name, brand, price, quantity)
        self.operation = operation

    def __str__(self):
        return f'Name: {self.name}\nBrand: {self.brand}\nPrice: {self.price}\nQuantity: {self.quantity}\nOperation: {self.operation}'

unit1 = Printer('printer', 'hp', 2000, 5, 'black and white printing')
unit2 = Scanner('scanner', 'Canon', 1200, 5, 'A3 scan')
unit3 = Copier('copier', 'Xerox', 1500, 1, 'color copy')
print(unit1)
print(unit2)
print(unit3)

# 5, 6
class Store:

    def __init__(self, name, brand, price, quantity, *args):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    @classmethod
    def reception(self, *args):
        try:
            unit_name = input(f'Enter the name: ')
            unit_brand = input(f'Enter the brand: ')
            unit_price = float(input(f'Enter price of a machine: '))
            unit_quantity = int(input(f'Enter amount of the machines: '))
        except ValueError:
            print('Not a number')
        return f'Name: {unit_name}, Brand: {unit_brand}, Price: {unit_price}, Quantity: {unit_quantity}'

'''
Моя идея заключалась в том, что при вводе данных через input можно было распределить технику на различные склады по ее 
наименованию. Но у решения задачи я так и не нашла. 
'''

class Printer(Store):
    def __init__(self, name):
        self.printers = []
    def get_printer(self):
        if unit_name == printer:
            self.printers.append(unit_name)
        else:
            pass


print(Store.reception())


# 7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'The sum of z1 and z2 is: ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'The multiplication of  z1 and z2 is: ')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)