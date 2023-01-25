import random
import csv
import json
import pandas


# 1. Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем результат преобразовать
# в байтовый вид в кодировке 'Latin-1' и затем результат снова декодировать в строку (вывести на экран)

print('\n1 задание:\n')

a = b'r\xc3\xa9sum\xc3\xa9'; b = a.decode('utf-8'); c = b.encode('Latin1'); d = c.decode('Latin1')
print(f'Исходная: {a} \nDecode utf-8: {b}\nEncode latin-1: {c}\nDecode latin-1: {d}')



# 2. Ввести с клавиатуры 4 строки и сохранить их в 4 разных переменные. Создать файл и записать в него
# первые 2 строки и закрыть файл. Затем открыть файл на редактирование и дозаписать оставшиемя 2 строки.
# В итоговом файле должно быть 4 строки, каждая должна начинаться с новой строки.

print('\n2 задание:\n')

text1, text2, text3, text4 = [input(f'Введите текст #{num}: ') for num in range(1, 5)]

with open('test.txt', 'w') as file_w:
    file_w.writelines([text1 + '\n', text2 + '\n'])
    file_w.close()

with open('test.txt', 'a') as file_a:
    file_a.writelines([text3 + '\n', text4])
    file_a.close()



# 3. Создать словарь в качестве ключа которого будет 6-ти значное значеное число (ID), а в качестве
# значение кортеж состоящий из 2-х элементов - имя (str), возраст (int). Сделать около 5 - 6
# элементов словаря. Записать данный словарь на диск в json-файл.

print('\n3 задание:\n')

template = {f'{random.randint(1, 100000):06}': (random.choice(['Петя', 'Коля', 'Вася', 'Таня', 'Катя']),
            random.randint(1, 99)) for _ in range(5)}

with open('temp.json', 'w') as file: json.dump(template, file, ensure_ascii=False); file.close()



# 4. Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой которого
# озаглавив каждый столбец и добавив новый столбец 'телефон'

print('\n4 задание:\n')


with open('temp.json', 'r') as file_j:
    in_json = json.load(file_j)

    data = [[f'#{num}', key, in_json[key][0], in_json[key][1],
             '{}{}{}-{}{}-{}{}'.format(*str(random.randint(1000000, 9999999)))]
            for num, key in enumerate(in_json, start=1)]

    file_j.close()

with open('temp.csv', 'w') as file_c:
    writer = csv.writer(file_c)
    writer.writerow(['NUM', 'ID', 'NAME', 'AGE', 'PHONE'])

    for line in data:
        writer.writerow(line)

    file_c.close()



# 5. Прочитать сохраненный csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими
# данными не нужен. Таблица должна выглядеть как на примере.

print('\n5 задание:\n')

with open('temp.csv', 'r') as file_c:

    data_l = csv.reader(file_c)
    data_s = dict()

    for x in data_l: data_s['' if x[0] == 'NUM' else 'Person ' + x[0][-1]] = x[1:3] + x[-1:]

data = pandas.DataFrame(data_s)
data.to_excel('temp.xlsx')
