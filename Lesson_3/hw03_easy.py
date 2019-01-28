
__author__ = 'Лезин Денис Андреевич'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def rnd(num, n):
    frac_part = num % 1 * (10 ** n)
    if frac_part % 1 * 10 // 1 > 4:
        frac_part += 1
    return (num // 1) + (frac_part // 1 * (10 ** -n))

num = float(input('Input decimal number: '))
n = int(input('Input number of digits: '))

print(rnd(num, n))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_func(num):
    def sm_func(num1):
        sm = 0
        for elm in num1:
            sm = sm + int(elm)
        return sm
    if sm_func(num[:3]) == sm_func(num[3:]):
        return 'You are Lucky!'
    else:
        return 'Sorry? Not your day...'

num = input('Enter your lucky number: ')
print(lucky_func(num))





