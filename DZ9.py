
# 1. Создать свой класс данных
# 2. Добавить в класс статикметод
# 3. Добавить в класс классметод

from dataclasses import dataclass, field

UP_PRICE = 0.2                              # глобальная константа для вычисления розничной стоимости

@dataclass
class Book:

    tot_book = 0                            # всего книг в магазине

    author: str                             # автор книги
    name: str                               # название книги
    price: float                            # цена закупки книги
    sel: float = field(init=False)          # розничная цена книги
    count: int = field(init=False)          # порядковый номер

    def __post_init__(self):

        Book.tot_book += 1
        self.count = Book.tot_book
        self.sel = round(self.price * UP_PRICE, 2)

    def get_info(self):
        return f'ID: {self.count}\nАвтор книги: {self.author}\nНазвание книги: {self.name}\n' \
               f'Стоимость закупки: {self.price}$\nДобавочная стоимость: {self.sel}$\n' \
               f'Стоимость реализации: {self.price + self.sel:.2f}$'

    @classmethod
    def get_count(cls):     # Возвращает общее количество книг в магазине

        return f'Всего книг магазине: {Book.tot_book}'

    @staticmethod
    def get_up_price(arg):  # Рассчитать стоимость книги в розницу

        return f'При стоимости закупки {arg} стоимость книги в розницу: {round(arg + arg * UP_PRICE, 2)}'


book_DM = Book(author='Джордж Мартин', name='Ветра зимы', price=27.1)
book_AD = Book(author='Александр Дюма', name='Граф Монте-Кристо', price=34.2)
book_FD = Book(author='Фёдор Достоевский', name='Идиот', price=12.7)


print(book_DM.get_info())           # >>> ID: 1 / Автор книги: Джордж Мартин / Название книги: Ветра зимы ...
print(Book.get_count())             # >>> Всего книг магазине: 3
print(Book.get_up_price(23.1))      # >>> При стоимости закупки 23.1 стоимость книги в розницу: 27.72


# 4. Создать метакласс

class Meta(type):
    def __new__(cls, name, s_class, attrib):
        return type(name, s_class, attrib)

New = Meta('NEW CLASS', (), {'some1': 111, 'some2': 222, 'get_info': lambda self: f'{self.some1} {self.some2}'})

print(type(New))                    # >>> <class 'type'>

obj_1 = New()
print(New.__dict__)                 # >>> {'some1': 111, 'some2': 222, 'get_info': <function <lambda> ...
print(obj_1.some1, obj_1.some2)     # атрибуты класса экземпляра # >>> 111 222
print(obj_1.get_info())             # метод класса # >>> 111 222

