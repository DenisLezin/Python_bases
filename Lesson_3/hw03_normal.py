__author__ = 'Лезин Денис Андреевич'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib_func(n, m):
    fib1 = 1
    fib2 = 1
    i = 2
    lst_fib = []
    while i <= m:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        if i >= n:
            lst_fib.append(fib1)
        i += 1
    return lst_fib

print(fib_func(4, 6))

def fib_func(n, m):
    lst_fib = []
    def fib_recur(num):
        if num == 1 or num ==2:
            return 1
        return fib_recur(num - 1) + fib_recur(num - 2)
    for i in range(n, m + 1):
        lst_fib.append(fib_recur(i))
    return lst_fib

n = int(input('Input element to start n = '))
m = int(input('Input final element m = '))
print(fib_func(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_func(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst

lst = [272, 54, 255, 479, 591, 830, 900, 147, 287, 63, 695, 579, 490, 262, 218, 121, 481, 732, 123, 590]
print(sort_func(lst))

#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


