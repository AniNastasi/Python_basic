#1
my_list = [1, 'ID', 23, '215', None]
print(my_list)
for el in my_list:
    print(el, type(el))

#2
ls = input('Enter list: ').split()
ls[:-1:2], ls[1::2] = ls[1::2], ls[:-1:2]
print(ls)

#3.1
li = [0, 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
p = int(input('Enter a month in form of number: '))
for i in range(0, 1):
    i = p
    print(li[i])

#3.2
di = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
k = int(input('Enter a month in form of number: '))
print(di[k])

#4
st = input('Enter any sentence: ').split()
print(st)
for i, el in enumerate(st, 1):
    print(i, el[0:10])

#5
num1 = [2, 35, 3, 76, 4.8]
num2 = sorted(num1)
print(num2)
for el in range(1):
    a = int(input('Enter a natural number: '))
    num1.append(a)
num3 = sorted(num1)
print(num3)

#5.1 Я решила также попробовать с запрашиваемым списком
# b = list(input('Enter a set of natural number: ').split(', '))
# print(b)
# c = sorted(b) #Если я использую просто sorted, то у меня в итоге сортируются пробелы тоже, поэтому я примерила split
# print(c) #Но на выходе у меня сортируются числа по первой цифреб т.е. например: 1, 11, 2, 24, 3
#
# for el in b:
#     d = int(el)
#     print(d)
#     e = ', '.join(el)
#     print(e)

#6 Это все на что хватило моей логики
while True:
    my_di = {}
    my_di['item'] = input('Enter an item. If there is nothing to enter, type "no": ')
    my_di['price'] = float(input('Enter a price. If there is nothing to enter, type "0": '))
    my_di['quantity'] = float(input('Enter a quantity. If there is nothing to enter, type "0": '))
    my_di['unit'] = input('Enter an unit. If there is nothing to enter, type "no": ')
    if my_di['item'] == 'no':
        break
    for key, value in my_di.items():
        print (f'{key}: {value}')
    print(my_di)














