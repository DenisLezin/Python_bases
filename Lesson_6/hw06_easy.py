'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''

class Worker:
    def __init__(self, name, surname, revenue):
        self.name = name
        self.surname = surname
        self.revenue = revenue
        self._income = {'salary': float(self.revenue.split()[0]),
                       'bonus': float(self.revenue.split()[1])}
        self.bonus = self._income['bonus']


worker1 = Worker('Dmitry', 'Lee', '50000 10000')

print(worker1.__dict__)
# __dict__ выводит информацию обо всех аттрибутах класса и их значениях в виде словаря

'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Position(Worker):
    def __init__(self, name, surname, revenue):
        Worker.__init__(self, name, surname, revenue)
        self.percent = self._income['bonus'] / self._income['salary']

    @property
    def salary(self):
        return self._income['bonus'] / self.percent


worker2 = Position('Andrey', 'Zolotov', '60000 6000')

print(f'Премия = {worker2.percent * 100}%,\nОклад  = {worker2.salary}')

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Position1(Worker):
    def __init__(self, name, surname, age, revenue):
        Worker.__init__(self, name, surname, revenue)
        self.age = age

    def full_name(self):
        return self.name + ' ' + self.surname + ' ' + ', ' + str(self.age) + ' лет'

    def total_revenue(self):
        return self._income['salary'] + self._income['bonus']


worker3 = Position1('Irina', 'Elenkina', 35, '80000 8000')
print(f'{worker3.full_name()}\nДоход {worker3.total_revenue()}')
