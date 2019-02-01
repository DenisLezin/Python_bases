
__author__ = 'Лезин Денис Андреевичы'
# Все задачи текущего блока решите с помощью генераторов списков!

import random
#lst_zero = [random.randint(-10, 40) for _ in range(20)]

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [0, 1, 2, 3] --> [0, 1, 4, 9]

lst = [12, 13, 11, 5, 14, 18, 2, 3, 10, 4]
lst_new = [(i ** 2) for i in lst]
print(f'Old list = {lst}\nNew list = {lst_new}')


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst_fruits1 = ['apple', 'orange', 'banana', 'kiwi', 'grape']
lst_fruits2 = ['kiwi', 'plum', 'orange', 'apple']
lst_fruits3 = [i for i in lst_fruits1 if i in lst_fruits2]
print(lst_fruits3)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 2
# + Элемент неотрицательный
# + Элемент не кратен 3

lst = [random.randint(-10, 40) for _ in range(20)]
lst_new = [i for i in lst if i % 2 == 0 and i > 0 and not i % 3 == 0]
print(f'Old list = {lst}\nNew list = {lst_new}')


