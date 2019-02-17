'''
Задание_1. Создать класс. В конструктор передать два параметра - два числа.
Создать второй класс. В конструкторе первого предусмотреть создание
объекта второго класса. Кроме того, в первом классе предусмотреть три метода,
в которых делегировать получение остатка от деления, результата деления и целой
части от деления в методы второго класса (предусмотреть вычисление в соотв. методах
второго класса).
'''

class SecondClass:
    def div_mod(self, num1, num2):
        return num1 % num2
    def div_classic(self, num1, num2):
        return num1 / num2
    def div_ex(self, num1, num2):
        return num1 // num2


class FirstClass:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.SecC = SecondClass()

    def div_mod(self):
        return self.SecC.div_mod(self.num1, self.num2)
    def div_classic(self):
        return self.SecC.div_classic(self.num1, self.num2)
    def div_ex(self):
        return self.SecC.div_ex(self.num1, self.num2)


FC = FirstClass(10, 3)

print(FC.div_mod())
print(FC.div_classic())
print(FC.div_ex())


