import datetime
import time


# 1. Дан словарь, создать новый словарь, поменяв местами ключ значение.
print('\n1 задание:')

d1 = dict(a=1, b=2, c=3); print('Исходны словарь:', d1)
d2 = {val: key for key, val in d1.items()}; print('Измененный словарь:', d2)


# 2. Написать программу для нахождения факториала. Реализацию выполнить в виде рекурсивной функции.
print('\n2 задание:')

num = input('Введите число: ')
while not num.isdigit(): num = input(f'"{num}" ERROR! Повторите: ')
num = int(num)

print(f'Фактариал числа {num} =', eval('*'.join([str(x) for x in range(1, num + 1)]))) # факториал

def fac(x): return x * fac(x - 1) if x else 1 # факториал через рекурсию
print(f'Фактариал числа {num} =', fac(num))


# 3. Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать для подсчета функцию.
print('\n3 задание:')

def calc(num): return {x: num.count(x) for x in num}
for x, y in sorted(calc([4, 1, 1, 2, 2, 3]).items()): print(f'{x} - колличество в списке: {y}')


# 4. Сделать функцию, которая будет вызываться из генератора списков и по запросу к ней отдавать
# текущее время с задержкой в 1 сек. Количество элементов n запрашивать у пользователя.
print('\n4 задание:')

def now(): return datetime.datetime.strftime(datetime.datetime.now(), '%Y/%m/%d %H:%M:%S')
print([[time.sleep(1), now()][1] for _ in range(int(input('Колличество повторений: ')))])


# Бонус - часы
while True: time.sleep(1); print('\r' + str(time.ctime()),  end='')
