
__author__ = 'Лезин Денис Андреевич'
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
'''
import re
print(re.findall('[a-z]+', 'mtMmEZUOmcq'))

string = 'mtMmEZUOmcq'
ch = ''
lst = []
for i in string:
    if i.islower():
        ch += i
    else:
        if ch:
            lst.append(ch)
            ch = ''
if ch: lst.append(ch) 
print(lst)
'''
# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random
import re
num = ''.join([str(random.randint(0,9)) for _ in range(2500)])
seq_tmp = ''
seq = ''
prev = 10
'''
for i in num:
    if not seq_tmp or int(i) == prev:
        seq_tmp += i
    else:
        seq = seq_tmp if len(seq_tmp) > len(seq) else seq
        seq_tmp = i
        prev = int(i)

with open('test.txt', 'r+') as f:
    f.write(num)
'''
# найти самую длинную последовательность через re
digit_list = re.findall(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+', num)
print(num)
print(digit_list)
print(max(digit_list, key=len))

print(seq)
