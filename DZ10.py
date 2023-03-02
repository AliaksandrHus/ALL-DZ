
# 1 Создать калькулятор (реализовал калькулятор с графическим интерфейсом)
# 2 Обернуть его в try/except (обернул только те инструкции где могут быть исключения)

import tkinter.messagebox
import tkinter

width = 8                               # ширина кнопок
height = 2                              # высота кнопок

class Calc:

    main_line = ' '                     # линия ввода операндов / операторов
    dot_flag = True                     # блокировка точки

    def __init__(self):

        self.main_win = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_win)
        self.frame1 = tkinter.Frame(self.main_win)
        self.frame2 = tkinter.Frame(self.main_win)
        self.frame3 = tkinter.Frame(self.main_win)
        self.frame4 = tkinter.Frame(self.main_win)

        self.value = tkinter.StringVar()
        self.lab = tkinter.Label(self.frame, textvariable=self.value, width=width * 3, height=height)
        self.delete = tkinter.Button(self.frame, text='<', width=width // 2, height=height, command=self.co_del)
        self.clear = tkinter.Button(self.frame, text='ce', width=width // 2, height=height, command=self.clear)

        self.frame.pack()
        self.delete.pack(side='right')
        self.clear.pack(side='left')
        self.lab.pack(side='left')

        self.value.set(Calc.main_line)

        self.one = tkinter.Button(self.frame1, text='1', width=width, height=height, command=self.co1)
        self.two = tkinter.Button(self.frame1, text='2', width=width, height=height, command=self.co2)
        self.three = tkinter.Button(self.frame1, text='3', width=width, height=height, command=self.co3)
        self.split = tkinter.Button(self.frame1, text='/', width=width, height=height, command=self.split)

        self.frame1.pack()
        self.one.pack(side='left')
        self.two.pack(side='left')
        self.three.pack(side='left')
        self.split.pack(side='left')

        self.four = tkinter.Button(self.frame2, text='4', width=width, height=height, command=self.co4)
        self.five = tkinter.Button(self.frame2, text='5', width=width, height=height, command=self.co5)
        self.six = tkinter.Button(self.frame2, text='6', width=width, height=height, command=self.co6)
        self.multiply = tkinter.Button(self.frame2, text='*', width=width, height=height, command=self.multiply)

        self.frame2.pack()
        self.four.pack(side='left')
        self.five.pack(side='left')
        self.six.pack(side='left')
        self.multiply.pack(side='left')

        self.seven = tkinter.Button(self.frame3, text='7', width=width, height=height, command=self.co7)
        self.eight = tkinter.Button(self.frame3, text='8', width=width, height=height, command=self.co8)
        self.nine = tkinter.Button(self.frame3, text='9', width=width, height=height, command=self.co9)
        self.minus = tkinter.Button(self.frame3, text='-', width=width, height=height, command=self.minus)

        self.frame3.pack()
        self.seven.pack(side='left')
        self.eight.pack(side='left')
        self.nine.pack(side='left')
        self.minus.pack(side='left')

        self.res = tkinter.Button(self.frame4, text='=', width=width, height=height, command=self.res)
        self.zero = tkinter.Button(self.frame4, text='0', width=width, height=height, command=self.zero)
        self.dot = tkinter.Button(self.frame4, text='.', width=width, height=height, command=self.dot)
        self.add = tkinter.Button(self.frame4, text='+', width=width, height=height, command=self.add)

        self.frame4.pack()
        self.res.pack(side='left')
        self.zero.pack(side='left')
        self.dot.pack(side='left')
        self.add.pack(side='left')

        tkinter.mainloop()

    def co_del(self):

        try:        # перехват исключения при удалении символа из линии ввода

            if Calc.main_line[-1] == '.': Calc.dot_flag = True

            Calc.main_line = Calc.main_line[:-1]
            self.value.set(Calc.main_line)

        except IndexError:

            tkinter.messagebox.showinfo(title='Внимание!', message='Хватит тыкать! Поле уже очищено! ')
            Calc.main_line = ' '
            self.value.set(Calc.main_line)


    def clear(self):

        Calc.main_line = ' '
        self.value.set(Calc.main_line)
        Calc.dot_flag = True

    def co1(self):
        Calc.main_line += '1'
        self.value.set(Calc.main_line)

    def co2(self):
        Calc.main_line += '2'
        self.value.set(Calc.main_line)

    def co3(self):
        Calc.main_line += '3'
        self.value.set(Calc.main_line)

    def split(self):

        if Calc.main_line[-1].isdigit() or Calc.main_line[-1] == '.':
            Calc.main_line += ' / '
            self.value.set(Calc.main_line)
            Calc.dot_flag = True

    def co4(self):
        Calc.main_line += '4'
        self.value.set(Calc.main_line)

    def co5(self):
        Calc.main_line += '5'
        self.value.set(Calc.main_line)

    def co6(self):
        Calc.main_line += '6'
        self.value.set(Calc.main_line)

    def multiply(self):

        if Calc.main_line[-1].isdigit() or Calc.main_line[-1] == '.':
            Calc.main_line += ' * '
            self.value.set(Calc.main_line)
            Calc.dot_flag = True

    def co7(self):
        Calc.main_line += '7'
        self.value.set(Calc.main_line)

    def co8(self):
        Calc.main_line += '8'
        self.value.set(Calc.main_line)

    def co9(self):
        Calc.main_line += '9'
        self.value.set(Calc.main_line)

    def minus(self):

        if Calc.main_line[-1].isdigit() or Calc.main_line[-1] == '.':
            Calc.main_line += ' - '
            self.value.set(Calc.main_line)
            Calc.dot_flag = True

    def res(self):

        try:                            # перехват исключения при расчете уравнения

            if any([True for x in '/*+-' if x in Calc.main_line]) and Calc.main_line[-2] not in '/*+-':
                Calc.main_line = str(eval(Calc.main_line))
                self.value.set(Calc.main_line)
                if '.' in Calc.main_line:
                    Calc.dot_flag = False

        except ZeroDivisionError:       # исключение деления на ноль

            tkinter.messagebox.showerror(title='Error', message='Делить на ноль нельзя!')

        except Exception:               # другие исключения / к примеру >>> 25 / 003

            tkinter.messagebox.showerror(title='Error', message='Неизвестная ошибка!\nПроверьте исходные данные!')

    def zero(self):
        Calc.main_line += '0'
        self.value.set(Calc.main_line)

    def dot(self):

        if Calc.dot_flag:
            if Calc.main_line[-1] == ' ': Calc.main_line += '0.'
            else: Calc.main_line += '.'
            self.value.set(Calc.main_line)
            Calc.dot_flag = False

    def add(self):

        if Calc.main_line[-1].isdigit() or Calc.main_line[-1] == '.':
            Calc.main_line += ' + '
            self.value.set(Calc.main_line)
            Calc.dot_flag = True

x = Calc()


# 3 сделать свое исключение и подключить его к try / except

PAY_UP = 7                 # константа ставка час/заработок

class Error(Exception):

    def __init__(self, arg, value):
        self.error = arg
        self.value = value

    def __str__(self):
        if self.error == 'code 1': return f'Ошибка! Значение должно быть в цифрах / Вы ввели >>> {self.value}'
        elif self.error == 'code 2': return f'Ошибка! Значение не может быть меньше 0 / Вы ввели >>> {self.value}'
        elif self.error == 'code 3': return f'Ошибка! Значение не может быть больше 24 / Вы ввели >>> {self.value}'


def pay_calc():            # расчет заработка в день

    hours = input('Отработанные часы: ')

    if not hours.replace('-' if hours[0] == '-' else '', '').isdigit(): raise Error('code 1', hours)
    else: hours = int(hours)

    if hours < 0: raise Error('code 2', hours)
    elif hours > 24: raise Error('code 3', hours)
    else: return hours * PAY_UP


try: print(f'За сегодня вы заработали: {pay_calc()}$')
except Exception as error: print(error)

