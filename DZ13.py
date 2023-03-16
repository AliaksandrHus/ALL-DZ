
# 1 Создать БД с двумя таблицами, соеденить их JOIN`ом
# 2 Подключить функции к запросам

import sqlite3

base = sqlite3.connect('studio.db')
cur = base.cursor()
cur.execute('PRAGMA foreign_keys=ON')

cur.execute("""CREATE TABLE Profile (P_ProfileID INTEGER PRIMARY KEY NOT NULL,
                                      Description TEXT)""")

cur.execute("""CREATE TABLE Person (ID INTEGER PRIMARY KEY NOT NULL,
                                   NAME TEXT,
                                   AGE INTEGER,
                                   ProfileID INTEGER,
                                   FOREIGN KEY (ProfileID) REFERENCES Profile (P_ProfileID))""")

cur.execute("""INSERT INTO Profile (P_ProfileID, Description)
                                    VALUES (1, 'Менеджер'),
                                           (2, 'Дизайнер'),
                                           (3, 'Программист')""")

cur.execute("""INSERT INTO Person (ID, NAME, AGE, ProfileID)
                                   Values (1, 'Петя Шмыг', 26, 1),
                                          (2, 'Вася Клык', 39, 2),
                                          (3, 'Даша Март', 28, 2),
                                          (4, 'Саня Крот', 33, 2),
                                          (5, 'Катя Смог', 23, 3),
                                          (6, 'Таня Корд', 34, 3)""")

base.commit()

staff = cur.execute("""SELECT NAME, AGE, Description
                       FROM Person
                       INNER JOIN Profile ON P_ProfileID == ProfileID""")

for x in staff: print(f'фио: {x[0]} | возраст: {x[1]} | должность: {x[2]}')

# >>> фио: Петя Шмыг | возраст: 26 | должность: Менеджер
# >>> фио: Вася Клык | возраст: 39 | должность: Дизайнер
# >>> фио: Даша Март | возраст: 28 | должность: Дизайнер
# >>> фио: Саня Крот | возраст: 33 | должность: Дизайнер
# >>> фио: Катя Смог | возраст: 23 | должность: Программист
# >>> фио: Таня Корд | возраст: 34 | должность: Программист


cur.execute("""SELECT MAX(AGE) FROM Person""")
max_age = cur.fetchone(); print(f'Максимальный возраст сотрудника: {max_age[0]} лет')
# >>> Максимальный возраст сотрудника: 39 лет

cur.execute("""SELECT MIN(AGE) FROM Person""")
min_age = cur.fetchone(); print(f'Минимальный возраст сотрудника: {min_age[0]} лет')
# >>> Минимальный возраст сотрудника: 23 лет

cur.execute("""SELECT AVG(AGE) FROM Person""")
avg_age = cur.fetchone(); print(f'Средний возраст сотрудников: {avg_age[0]} лет')
# >>> Средний возраст сотрудников: 30.5 лет

cur.execute("""SELECT SUM(AGE) FROM Person""")
sum_age = cur.fetchone(); print(f'Общий возраст всех сотрудников: {sum_age[0]} года')
# >>> Общий возраст всех сотрудников: 183 года

cur.execute("""SELECT COUNT(*) FROM Person WHERE ProfileID == 1""")
man_count = cur.fetchone(); print(f'Количество менеджеров: {man_count[0]} чел')
# >>> Количество менеджеров: 1 чел

cur.execute("""SELECT COUNT(*) FROM Person WHERE ProfileID == 2""")
des_count = cur.fetchone(); print(f'Количество дизайнеров: {des_count[0]} чел')
# >>> Количество дизайнеров: 3 чел

cur.execute("""SELECT COUNT(*) FROM Person WHERE ProfileID == 3""")
pro_count = cur.fetchone(); print(f'Количество программистов: {pro_count[0]} чел')
# >>> Количество программистов: 2 чел
