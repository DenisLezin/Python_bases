
__author__ = 'Лезин Денис Андреевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.

print('Max number is ', max(input('Input int number: ')))



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

a = input('Input the first parameter: ')
b = input('Input the second parameter: ')
a = (a, b)
b = a[0]
a = a[1]
print('a = ', a, ', b = ', b)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4


import math

a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))

D = b ** 2 - 4 * a * c

if D < 0:
    print('D < 0, Дейсьвительных корней нет')
elif D == 0:
    x1 = round(-b / (2 * a), 4)
    x2 = x1
    print('D = 0, x1 = x2 = ', x1)
else:
    x1 = round((-b + math.sqrt(D)) / (2 * a), 4)
    x2 = round((-b - math.sqrt(D)) / (2 * a), 4)
    print('D = ', D, 'x1 = ', x1, ', x2 = ', x2)





