import random

# 1. Ввести предложение состоящие из двух слов. Поменять местами слова, добавить восклицательный знак
# в начало и конец, слова разделить 3 символами (пробел, восклицательный знак и еще пробел), вывести
# итоговое предложение на экран. Задание необходимо сделать 3-мя разными способами форматирования.

#text = input('Введите предложение из двух слов: ')

text = 'первое второе'
text = text.split(); text.reverse()

print('!%s ! %s!' % (text[0], text[1]))
print('!{} ! {}!'.format(*text))
print(f'!{text[0]} ! {text[1]}!')

print()

# 2. Написать программу, которая получит имя и возраст пользователя, проверяет возраст и выдает
# приветственное сообщение в зависимости от возраста.

# 3. Завернуть это в бесконечный цикл.

while True:

    print('Введите данные или "СТОП" что бы прервать:')
    name = input('Ваше имя: ')
    if name.lower() == 'стоп': break
    age = input('Ваш возраст: ')

    while not age.isdigit():
        print('ERROR - возраст должен содержать только цифры')
        age = input('Ваш возраст или "СТОП" что бы прервать: ')
        if age.lower() == 'стоп': break

    if age.lower() == 'стоп': break

    age = int(age)

    if age <= 0: print('Ошибка, повторите ввод!')
    elif 0 < age < 10: print(f'Привет шкет {name}!')
    elif 10 <= age < 18: print(f'Как жизнь {name}?')
    elif 18 <= age < 100: print(f'Что желаете {name}?')
    else: print(f'{name}, вы лжете - в наше время столько не живут!')

print()

# 4. Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n).
# Реализовать в 2-х вариантах: используя цикл while и цикл for.

num = input('Введите целое число: ')
while not num.isdigit(): print('Принимаем только цифры! Повторите ввод!'); num = input('Введите целое число: ')
num = int(num)

tot = 0
for _ in range(1, num + 1): tot += _ ** 3
print(f'Сумма кубов от 1 до {num} равна', tot)

tot, count = 0, 1
while count != num + 1: tot += count ** 3; count += 1
print(f'Сумма кубов от 1 до {num} равна', tot)

print()

# 5. Сделать программу в которой нужно угадать число.

maximum = 10
rand_num = random.randint(1, maximum)

try:

    player = int(input(f'Угадайте число от 1 до {maximum}: '))
    count = 1

    while rand_num != player:

        if player < rand_num: print('Больше!')
        else: print('Меньше!')
        player = int(input(f'Число от 1 до {maximum}: '))
        count += 1

    print(f'\nУгадал с {count} попытки! число {player}')

except ValueError:
    print(f'\nERROR: недопустимый символ в строке ввода!\nА число было {rand_num}')

