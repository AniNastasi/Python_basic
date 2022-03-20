# 1
# with open('t1.txt', 'w', encoding='utf-8') as f:
#     while True:
#         t = input('Enter some data: ')
#
#         if not t:
#             break
#         f.write(f'{t}\n')

# 2
# with open('t2.txt', 'r', encoding='utf-8') as f:
#     i = 0
#     for i, el in enumerate (f, 0):
#         i = i + 1
#         k = len(el)
#         print(el, end='')
#         print('Number of elements in the row is: ', k)
#     print('Total number of rows is: ', i)

# 3
# with open('t3.txt', 'r', encoding='utf-8') as f:
#     data = []
#     for i in f:
#         l = i.split()
#         ls = data.append(l)
#
#     di = {x[0]:float(x[1]) for x in data}
#     print(di)
#     print('list of staff with salary less then 20000:')
#     for key, value in di.items():
#         if value < 20000:
#             print(f'{key}: {value}')
#
#     su = sum(di.values())
#     print(f'total sum of salaries is: {su}')

# 4
# with open('t4.txt', 'r+', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')

# 5
# with open('t5.txt', 'w+', encoding='utf-8') as f:
#     f.write(input('Enter numbers space-separated: '))
#     f.seek(0)
#     text = f.read()
#     print(text)
#     t = text.split(' ')
#     su = 0
#     for i in t:
#         el = int(i)
#         su = su + el
#     print(su)

# 6
# with open('t6.txt', 'r', encoding='utf-8') as f:
#     di = {}
#     data = []
#     for i in f:
#         print(i, end='')
#         l = i.split(':')
#         ls = data.append(l)
#     print(data)
#
#     dic = {x[0]:x[1] for x in data}
#     print(dic)
#
#     for key, value in dic.items():
#         value = str(value[1:])
#         a = value.split(' ')
#         print(a) # Далее у меня нет идей как можно сделать.

# 7
with open('t7.txt', 'r', encoding='utf-8') as f:
    d = dict()
    data = []

    for line in f:
        print(line)
        el = line.split(' ')
        firm = el[0]
        profit = float(el[3]) - float(el[2])

        di = {firm: profit}
        d = d.append(di)
    print(data)








