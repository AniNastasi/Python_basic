# #1.1
# def fun1():
#     x1 = float(input('Enter a number: '))
#     x2 = float(input('Enter a number: '))
#
#     try:
#         a = x1 / x2
#         return a
#     except ZeroDivisionError:
#         return '0 cannot be divided'
#
# b = fun1()
# print(b)

#1.2 У меня не получается через if получить результат, все равно запрашивается exception.
# def fun2():
#     c1 = float(input('Enter a number: '))
#     c2 = float(input('Enter a number: '))
#
#     d = c1 / c2
#     if c2 == 0:
#         print('0 cannot be divided')
#     else:
#         return d
# f = fun2()
# print(f)

# #2
# def user(name, surname, year, city, email, tel):
#     print(f'name: {name}; surname: {surname}; year of birth: {year}; city: {city}; email: {email}; tel.: {tel}')
#
# user(name=input('Enter your name: '), surname=input('Enter your surname: '), year=input('Enter the year of your birth: '),
#      city=input('Enter city: '), email=input('Enter your email: '), tel=input('Enter you phone number: '))

#3
# def my_func(ls):
#     maxes = []
#     for el in ls:
#         maxi = max(ls)
#         ls.remove(maxi)
#         maxes.append(maxi)
#
#     return maxes
# ls = [10, 100, 30]
# r = my_func(ls)
# summ = sum(r)
# print(f'two maximum numbers are: {r}, the sum of them is: {summ}')

# 4.1
# def fun4(x, y):
#     r = x ** y
#     return r
# f4 = fun4(2, -3)
# print(f4)

# 4.2
# def fun5():
#     x = 2
#     a = x
#     y = -4
#
#     for y in range(abs(y)-1):
#         y = y + 1
#         x = (a * x)
#         res = 1 / x
#         print(x)
#     return res
#
# f5 = fun5()
# print(f5)


# #5
# def fun6():
#     sums = []
#     while True:
#         v1 = input('Enter a set of numbers: ').split()
#         sum1 = 0
#
#         for el in v1:
#             ele = int(el)
#             # print(ele)
#             sum1 = sum1 + ele
#             # print(sum1)
#
#             if ele == 0:
#                 return sum1, sums
#
#         a = sum1
#         s = sums.append(a)
#         b = sums
#         t_sum = sum(b)
#         print(f'sum of the set is: {a}')
#         print(f'list of sums is: {b}')
#         print(f'total sum of sets is: {t_sum}')
# p = fun6()
# print('end')

# #6
# def int_func():
#     f6 = input('Enter words with small letters: ')
#     word1 = f6.capitalize()
#     return word1
#
# t = int_func()
# print(t)

#7 У меня не получилось объединить в список выходные данный из цикла for
def int_func():
    ls = []
    f6 = list(input('Enter set of words with small letters: '). split())

    for ind in f6:
        word = ind.capitalize()
        print(word)
    return


    text = ls.append()

t = int_func()
print(t)
