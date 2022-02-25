# 1
# from sys import argv
#
# print(argv)
# path, n, wh, r, b = argv
# print(n, wh, r, b)
# wh, r, b = map(int, argv[2:])
# print('Name: ', n)
# print('Worker-hours: ', wh)
# print('Rate: ', r)
# print('Bonus: ', b)
# S = wh * r + b
# print('Salary: ', S)

# 2
# ls = [2, 7, 56, 48, 89, 65, 43, 21, 8]
# new_ls = [ls[i] for i in range(0, len(ls)-1) if ls[i] > ls[i - 1]]
# print(new_ls)

# 3
# lst = [i for i in range(20, 240) if i % 21 == 0]
# print(lst)

# 4
# ls = [2, 7, 56, 48, 89, 65, 43, 21, 8, 2, 2, 7]
# new_ls = [el for el in ls if ls.count(el) == 1]
# print(new_ls)

# 5
# my_ls = [j for j in range(100, 1001) if j % 2 == 0]
# print(my_ls)
# from functools import reduce
# sum_ls = reduce(lambda a, b: a * b, my_ls)
# print(sum_ls)

# 6
# from itertools import count, cycle
# c = float(input('Enter a number to start counts from: '))
# d = float(input('Enter a step to count with: '))
# e = float(input('Enter a number to end count with: '))
# for el in count(c, d):
#     if el > 10:
#         break
#     print(el)
#
# i = 0
# a = list(input('Enter elements to be cycled: '))
# b = int(input('Enter number of cycles: '))
# for el in cycle(a):
#     i = i + 1
#     if i > 10:
#         break
#     print(el)

# 7.1
# from math import factorial
# f = int(input('Enter a number factorial of which you want to find: '))
# li = [factorial(i) for i in range(1, f + 1)]
# print(li)
#
# # 7.2
# def gen():
#     for el in (factorial(i) for i in range(1, f + 1)):
#         yield el
# g = gen()
#
# for ind in g:
#     print(ind)