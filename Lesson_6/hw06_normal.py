'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
import math

class Triangle:
    def __init__(self, X1, X2, X3):
        self.X1 = X1
        self.X2 = X2
        self.X3 = X3
        
        
    def side(X1, X2): return math.sqrt((X2[0] - X1[0]) ** 2 + (X2[1] - X1[1]) ** 2) 

    A = side(X1, X2)
    B = side(X2, X3)
    C = side(X3, X1)
    
    perimetr = A + B + C
    _p = perimetr / 2
    high = (2 * math.sqrt(_p * (_p - A) * (_p - B) * (_p - C))) / A
    area = high * A / 2    
        

X1 = [1, 1]
X2 = [2, 3]
X3 = [4, 2]

tr = Triangle(X1, X2, X3)

print(tr.A, tr.B, tr.C)
print(tr.perimetr)
print(tr.high)
print(tr.area)
