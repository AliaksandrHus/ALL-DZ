
import time
import math

print('\n1 Задание\n')

# 1. Создать родительский класс auto, у которого есть атрибуты: brand, age, color, mark и weight. А так же методы:
# move, birthday и stop. Методы move и stop выводят на экран сообщения 'move' и 'stop', а birthday увеличивает
# атрибут age на 1. Атрибуты brand, age и mark являются обязательными прт объявлении объекта.

class Auto:

    def __init__(self, brand, age, mark, color=None, weight=None):

        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def birthday(self): self.age += 1
    def move(self): print('move')
    def stop(self): print('stop')


car1 = Auto('Ford', 17, 'Mustang', 'Black', 1600)

print('Auto:')
print('\ncar1:\n')

print(car1.__dict__)    # >>> {'brand': 'Ford', 'age': 17, 'mark': 'Mustang', 'color': 'Black', 'weight': 1600}
car1.birthday()         # >>> / age += 1 /
print(car1.__dict__)    # >>> {'brand': 'Ford', 'age': 18, 'mark': 'Mustang', 'color': 'Black', 'weight': 1600}

car1.move()             # >>> move
car1.stop()             # >>> stop


print('\n2 Задание\n')

# 2. Создать 2 класса truck и car, которые являются наследниками класса auto. Класс truck имеет дополнительный
# обязательный атрибут max_load. Переопределенный метод move, перед появлением надписи 'move' выводит надпись
# 'attention', его реализацию сделать при помощи оператора super. А также дополнительный метод load. При его
# вызове происходит пауза 1 сек затем выводиться сообщение 'load' и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появоения
# надписи 'move' должна появиться надпись 'max speed is "max-speed"'. Создать по 2 объекта для каждого из
# классов truck и car, проверить все их методы и атрибуты.


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):

        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self): print('attention move')
    def load(self): time.sleep(1); print('load'); time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):

        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self): print(f'move max speed is: {self.max_speed}')

print('Truck:')
print('\ncar2:\n')

car2 = Truck('Ford', 10, 'Explorer', 1750)

print(car2.__dict__)    # >>> {'brand': 'Ford', 'age': 10, 'mark': 'Explorer', 'color': None, 'weight': None, 'max_load': 1750}
car2.birthday()         # >>> / age += 1 /
print(car2.__dict__)    # >>> {'brand': 'Ford', 'age': 11, 'mark': 'Explorer', 'color': None, 'weight': None, 'max_load': 1750}

car2.load()             # >>> / sleep(1) / load / sleep(1)
car2.move()             # >>> attention move
car2.stop()             # >>> stop

print('\ncar3:\n')

car3 = Truck('Ford', 5, 'F-150', 2350)

print(car3.__dict__)    # >>> {'brand': 'Ford', 'age': 5, 'mark': 'F-150', 'color': None, 'weight': None, 'max_load': 2350}
car3.birthday()         # >>> / age += 1 /
print(car3.__dict__)    # >>> {'brand': 'Ford', 'age': 6, 'mark': 'F-150', 'color': None, 'weight': None, 'max_load': 2350}

car3.load()             # >>> / sleep(1) / load / sleep(1)
car3.move()             # >>> attention move
car3.stop()             # >>> stop

print('\nCar:')
print('\ncar4:\n')

car4 = Car('Ford', 1, 'Focus', 259)

print(car4.__dict__)    # >>> {'brand': 'Ford', 'age': 1, 'mark': 'Focus', 'color': None, 'weight': None, 'max_speed': 259}
car4.birthday()         # >>> / age += 1 /
print(car4.__dict__)    # >>> {'brand': 'Ford', 'age': 1, 'mark': 'Focus', 'color': None, 'weight': None, 'max_speed': 259}

car4.move()             # >>> move max speed is: 259
car4.stop()             # >>> stop

print('\nCar:')
print('\ncar5:\n')

car5 = Car('Ford', 27, 'Probe', 221)

print(car5.__dict__)    # >>> {'brand': 'Ford', 'age': 27, 'mark': 'Probe', 'color': None, 'weight': None, 'max_speed': 221}
car5.birthday()         # >>> / age += 1 /
print(car5.__dict__)    # >>> {'brand': 'Ford', 'age': 27, 'mark': 'Probe', 'color': None, 'weight': None, 'max_speed': 221}

car5.move()             # >>> move max speed is: 221
car5.stop()             # >>> stop

print('\n3 Задание\n')

# 3. Для рассмотреного на уроке класса Circle реализовать метод производящий вычтание двух окружностей,
# вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым радиусом, то
# результатом вычитания будет точка Point.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self): return (self.x**2 + self.y**2) ** 0.5


class Circle(Point):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self): return self.radius - (self.x**2 + self.y**2) ** 0.5

    def area(self): return math.pi * self.radius ** 2

    def circumference(self): return math.pi * (self.radius * 2)

    def __isub__(self, other):

        self.x -= other.x
        self.y -= other.y
        self.radius -= other.radius

        return Circle(self.x, self.y, self.radius) if self.radius > 0 else Point(self.x, self.y)


circle1 = Circle(10, 20, 30)
circle2 = Circle(20, 30, 20)

circle3 = circle1.__isub__(circle2)
print(f'Результат: {circle3.__dict__}, {type(circle3)}')
# >>> Результат: {'x': -10, 'y': -10, 'radius': 10}, <class '__main__.Circle'>

circle4 = circle1.__isub__(circle1)
print(f'Результат: {circle4.__dict__}, {type(circle4)}')
# >>> Результат: {'x': 0, 'y': 0}, <class '__main__.Point'>

