'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''

class DictBuilder:
    def __init__(self, dict1, dict2):
        #self.dict1 = dict1
        #self.dict2 = dict2
        #self.d = {}
        i = 0
        for key in dict1:
            setattr(self, key, dict2[i])
            i += 1


dict = DictBuilder(['name', 'surname', 'age'], ['Dmitry', 'Lee', 25])
print(dict.__dict__)
print(f'{dict.surname} {dict.name}, age {dict.age}')

'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''

class ListClearWrapper:
    def __init__(self, lst):
        self.wrapped = lst

    def __getattr__(self, attr):
        return getattr(self.wrapped, attr)

lst = ListClearWrapper(['a', 'f', 34])
print(lst.wrapped)
lst.clear()
print(lst.wrapped)

