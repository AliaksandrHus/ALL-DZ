
import re

# 1 Создать генератор геометрической прогрессии
# 2 Подключить дебагинг (подключил, чес. слово)


def progression(x=1, count=1):
    yield f'{count}: {x}'
    while True: x *= 2; count += 1; yield f'{count}: {x}'


a = progression()

print('Нажмите Enter для продолжения или введите стоп/stop для завершения')

while True:
    stop = input(f'Позиция #{next(a)} ')
    if stop.lower() in ['стоп', 'stop']: print('END'); break

# >>> Нажмите Enter для продолжения или введите стоп/stop для завершения
# >>> Позиция #1: 1
# >>> Позиция #2: 2
# >>> Позиция #3: 4
# >>> Позиция #4: 8 stop >>> break
# >>> END


# 3 Сделать функцию для фильтрации емейла (ркгуляркой). Правила валидации 'username@hostname':

# - username может содержать: латиницу, цифры, ! # % & ' * + - / = ? ^ _ ` { | } ~
# и точку за исключением первого и последнего знака которая не может повторяться

# - hostname состоит из нескольких компонентов, разделенных точкой и не превышающих 63 символа
# Компоненты, в свою очередь, состоят из латинских букв, цифр и дефисов, причем дефисы не могут
# быть в начале или в конце компонента.

step1 = r"(?:[a-z0-9!#$%&'*+=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+=?^_`{|}~-]+)*)@(?:[a-z0-9]+(?:-[a-z0-9]+)*)\.[a-z]{2,5}"
step2 = r"@.{1,63}\."


def check_email(arg): return True if re.fullmatch(step1, arg) and re.search(step2, arg) else False


email_list = ['abcdf@mail.ru', '1abcdf@mail.ru', 'a1bcdf@mail.ru',  'abcdf1@mail.ru',
              '!abcdf@yandex.by', 'a#bcdf@yandex.by', 'abcdf*@yandex.by', 'abcdf@yan-dex.by',
              'ab.df@gmail.com', 'a.b.d.f@gmail.com', '1ab.df2@gmail.com', 'abdf@gmail1.com',
              'abdf@123456789a123456789b123456789c123456789d123456789f123456789-063.com',
              '.abcdf@mail.ru', 'abcdf.@mail.ru', 'abcdf@mail', 'abcdf@.ru',
              'abcdf@-yandex.by', 'abcdf@yandex-.by', 'abcdf@y?ndex.by', '!abcdfyandex.by',
              'abdf@g--mail.com', 'ab..df@gmail.com', 'abdf@_gmail.com', 'abdf@gma!l.com',
              'abdf@123456789a123456789b123456789c123456789d123456789f123456789f-064.com']


for email in email_list: print(f'{check_email(email)}: {email}')

# >>> True: abcdf@mail.ru
# >>> True: 1abcdf@mail.ru
# >>> True: a1bcdf@mail.ru
# >>> True: abcdf1@mail.ru
# >>> True: !abcdf@yandex.by
# >>> True: a#bcdf@yandex.by
# >>> True: abcdf*@yandex.by
# >>> True: abcdf@yan-dex.by
# >>> True: ab.df@gmail.com
# >>> True: a.b.d.f@gmail.com
# >>> True: 1ab.df2@gmail.com
# >>> True: abdf@gmail1.com
# >>> True: abdf@123456789a123456789b123456789c123456789d123456789f123456789-063.com

# >>> False: .abcdf@mail.ru
# >>> False: abcdf.@mail.ru
# >>> False: abcdf@mail
# >>> False: abcdf@.ru
# >>> False: abcdf@-yandex.by
# >>> False: abcdf@yandex-.by
# >>> False: abcdf@y?ndex.by
# >>> False: !abcdfyandex.by
# >>> False: abdf@g--mail.com
# >>> False: ab..df@gmail.com
# >>> False: abdf@_gmail.com
# >>> False: abdf@gma!l.com
# >>> False: abdf@123456789a123456789b123456789c123456789d123456789f123456789f-064.com
