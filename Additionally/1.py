
# Придумать задачу на каждый тип данных.
# В каждой задаче(на каждый тип), используйте минимум один метод работы с этим типом данных.

float_list = [3.141592, '.as_integer_ratio()', '.is_integer()', '.hex()']
str_list = ['"Текст для примера"', '.upper()', '.split()', '.find("для")']
list_list = [['a', 'c', 'b'], '.count("a")', '.pop()', '.index("b")']
tuple_list = [('1', '2', '1'), '.count("1")', '.index("2")']
dict_list = [{'one': 1, 'two': 2}, '.get("two")', '.keys()', '.items()']
set_list = [{1, 2, 3}, '.pop()', '.isdisjoint({4, 5, 6})', '.discard("x")']

all_type = [float_list, str_list, list_list, tuple_list, dict_list, set_list]

for a in all_type:
    print(type(a[0]))
    for b in a[1:]:
        print(f'{a[0]}{b} >>> {eval(f"{a[0]}{b}")}')
    print()
