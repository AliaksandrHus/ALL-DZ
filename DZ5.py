from datetime import datetime

# 1. Написать лямбда-функцию определяющую четное/нечетное.
# Функция принимает параметр (число) и если четное то выдает слова "четное", если нет - то "нечетное".
print('\n1 задание:\n')

res = lambda num: 'четное' if num % 2 == 0 else 'нечетное'

for x in range(1, 6): print(x, res(x))

# 2. Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку.
# В качестве функции в map использовать lambda.
print('\n2 задание:\n')

num = [1, 2, 3, 4, 5]
res = list(map(lambda x: str(x), num))
print(f'input: {num}\noutput: {res}')

# 3. При помощи функции filter() из кортежа слов отфильтровать только те, которые являются палиндромами.
print('\n3 задание:\n')

words = ('око', 'омут', 'комок', 'аромат', 'шалаш', 'жук', 'заказ')
res = list(filter(lambda x: x == x[::-1], words))
print(f'input: {words}\noutput: {res}')

# 4. Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
print('\n4 задание:\n')

def dec(fun):
    def wrapper():
        start = datetime.now()
        fun()
        print(f'Скорость выполнения {str(fun).split()[1]} =', datetime.now() - start)
    return wrapper

@dec
def cycle():
    temp = []
    for x in range(1000):
        if x % 2 == 0: temp.append(x)

@dec
def listing():
    temp = [x for x in range(1000) if x % 2 == 0]

cycle()
listing()

# 5. Сделать функцию которая на вход принимает строку. Анализирует ее исключительно методом .isdigit()
# без дополнительных библиотек и переводит строку в число. Функция умеет распознавать отрицательные числа и дроби.
# Вывод в формате: -.777 >>> Вы ввели отрицательное дробное число: -0.777
print('\n5 задание:\n')


def get_check(x):

    if x[0:2] == '-.' and x.count('.') < 2 and x.count('-') < 2: x = '-0.' + x[2:]
    elif x[0] == '.' and x.count('.') < 2: x = '0' + x
    elif x[-1] == '.' and x.count('.') < 2: x += '0'

    m = 'положительное' if x[0] != '-' else 'отрицательное'
    s = 'целое' if x.count('.') == 0 else 'дробное'

    if x.count('-') > 1 or x.count('.') > 1 \
            or not x.replace('-', '').replace('.', '').isdigit(): m, s = 'некоректное', '\b'

    if s == 'целое': x = int(x)
    elif s == 'дробное': x = float(x)

    return f'Вы ввели {m} {s} число: {x}'


for x in ['-1.00', '.2.', '323', '.214', '3a3', '-8', '--.34', '-.3']: print(get_check(x))
