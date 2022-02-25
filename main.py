#1
import math

Gene = input('Gene:')
sample_id = input('Sample ID: ')
Samp = float(input('Gene expression in the sample: '))
C = float(input('Gene expression in the control: '))
FC = (Samp / C)
logFC = math.log(FC , 10) # Очень хотела сделать расчет экспрессии генов, поэтому чуть подсмотрела, как считать.
print('Differential gene expression is: ' , logFC)
if logFC > 0:
    print('upregulation')
else:
    print('downregulation')

#2
t = int(input('Enter time, sec: '))
H = t // 3600
M = t % 3600 // 60
S = t % 60
print(H, ':', M, ':', S)

#3
n = int(input('Enter a positive number: '))
n1 = str(n)
n2 = int(n1 * 2)
n3 = int(n1 * 3)
sum = n + n2 + n3
print('n+nn+nnn: ', n1, '+', n2, '+', n3, '=', sum)

#4
num = int(input('Enter a positive number: '))
while True:
    dig = num % 10
    num = num // 10
    print(dig)
    if dig > dig:
        print(dig)
    else:
        break
print('end')

#5
I = float(input('Enter Income: '))
E = float(input('Enter Expenses: '))
P = I - E
print('Profit is: ', P)
if P > 0:
    Eff = P / I
    print('Efficiency is: ', Eff)
    N = int(input('Enter staffing level: '))
    PP = P / N
    print('Profit pro Person is: ', PP)
else:
    print('Enterprise is unprofitable')

#6
R = float(input('Enter your original distance: '))
DR = float(input('Enter the desirable distance: '))
P = float(input('Enter a percentage of the distance increase: '))
count = 1
while R <= DR:
    R = R + 0.01 * P * R
    count = count + 1
    print(count, R)
    if R > DR:
        print('The aim will be reached on ', count, 'day')
        break
        print(count)




