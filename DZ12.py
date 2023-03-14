import sqlite3

# 1 Создать таблицу со студентами в БД
# 2 Создать таблицу аудиторий в БД
# 3 Сделать связь таблиц

table = sqlite3.connect('TMS_DZ13.db')
cur = table.cursor()
cur.execute("PRAGMA foreign_keys=ON")


# Таблица аудиторий
cur.execute("""CREATE TABLE Classroom (RoomID INTEGER PRIMARY KEY NOT NULL,
                                       RoomNum INTEGER,
                                       Floor INTEGER,
                                       GroupNum TEXT)""")

# Таблица учащихся # Связь таблиц - внешний ключ RoomID
cur.execute("""CREATE TABLE Students (ID INTEGER PRIMARY KEY NOT NULL,
                                      FullName TEXT,
                                      GroupNum TEXT,
                                      Curse TEXT,
                                      RoomID INTEGER,
                                      FOREIGN KEY (RoomID) REFERENCES Classroom (RoomID))""")

# Заполнение таблицы аудиторий
cur.execute("""INSERT INTO Classroom (RoomID, RoomNum, Floor, GroupNum)
                                      VALUES (1, 202, 2, 'P85'),
                                             (2, 373, 3, 'E63'),
                                             (3, 424, 4, 'D95')""")
# Заполнение таблицы учащихся
cur.execute("""INSERT INTO Students (ID, FullName, GroupNum, Curse, RoomID)
                                     VALUES (1, 'Петя Шмыг', 'P85', 'Python ', 1),
                                            (2, 'Вася Клык', 'P85', 'Python ', 1),
                                            (3, 'Даша Март', 'P85', 'Python ', 1),

                                            (4, 'Саня Крот', 'E63', 'English', 2),
                                            (5, 'Катя Смог', 'E63', 'English', 2),
                                            (6, 'Таня Корд', 'E63', 'English', 2),

                                            (7, 'Гоша Краб', 'D95', 'Design ', 3),
                                            (8, 'Паша Мост', 'D95', 'Design ', 3),
                                            (9, 'Лиза Стеб', 'D95', 'Design ', 3)""")

table.commit()

# Вывод всех аудиторий
classroom = cur.execute('SELECT * FROM Classroom')
for x in classroom: print(f'ID: {x[0]} | номер кабинета: {x[1]} | этаж: {x[2]} | закрепленная группа: {x[3]}')

# >>> ID: 1 | номер кабинета: 202 | этаж: 2 | закрепленная группа: P85
# >>> ID: 2 | номер кабинета: 373 | этаж: 3 | закрепленная группа: E63
# >>> ID: 3 | номер кабинета: 424 | этаж: 4 | закрепленная группа: D95


# Вывод всех учащихся
students = cur.execute('SELECT * FROM Students')
for x in students: print(f'ID: {x[0]} | ФИО: {x[1]} | группа: {x[2]} | программа: {x[3]} | ID аудитории: {x[4]}')

# >>> ID: 1 | ФИО: Петя Шмыг | группа: P85 | программа: Python  | ID аудитории: 1
# >>> ID: 2 | ФИО: Вася Клык | группа: P85 | программа: Python  | ID аудитории: 1
# >>> ...
# >>> ID: 9 | ФИО: Лиза Стеб | группа: D95 | программа: Design  | ID аудитории: 3


# Вывод учащихся с внешним ключом
all_p85 = cur.execute("""SELECT Students.FullName, Students.Curse, Classroom.RoomNum, Classroom.Floor 
                         FROM Students, Classroom
                         WHERE Students.RoomID == Classroom.RoomID""")

for x in all_p85: print(f'ФИО: {x[0]} | программа: {x[1]} | номер кабинета: {x[2]} | этаж: {x[3]}')

# >>> ФИО: Петя Шмыг | программа: Python  | номер кабинета: 202 | этаж: 2
# >>> ФИО: Вася Клык | программа: Python  | номер кабинета: 202 | этаж: 2
# >>> ...
# >>> ФИО: Лиза Стеб | программа: Design  | номер кабинета: 424 | этаж: 4
