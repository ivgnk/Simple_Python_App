"""
calc.py
https://github.com/kalexal-kaa/python-projects/tree/main/projects
"""

# calc.py - a Python calculator
from tkinter import *

ppady=10

# the main class
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num == True:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.' and '.' in temp:
                    return
            self.current = temp + temp2
            while len(self.current) > 1 and self.current[0] == '0' and self.current[1] != '.':
                self.current = self.current[1:]
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "minus":
            self.total -= self.current
        elif self.op == "times":
            self.total *= self.current
        elif self.op == "divide" and self.current:
            self.total /= self.current
        else:
            self.total = 0
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        elif self.eq == False:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        if self.new_num == False:
            self.current = "0"
            self.display(0)
            self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.new_num = False
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)


class My_Btn(Button):
    def btn_cmd(self, num):
        self["command"] = lambda: sum1.num_press(num)


sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Калькулятор")
root.resizable(width=False, height=False)
text_box = Entry(calc, justify=RIGHT)
# text_box.grid(row = 0, column = 0, columnspan = 3, pady = ppady)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = ppady)
text_box.insert(0, "0")

# make the buttons
numbers = "789456123"
i = 0
# Отдельно прямоугольный блок цифр numbers
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(My_Btn(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = ppady)
        bttn[i].btn_cmd(numbers[i])
        i += 1
# Недостающая цифра == 0
bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 1, pady = ppady)

bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 1, column = 3, pady = ppady)

bttn_mult = Button(calc, text = "x")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 2, column = 3, pady = ppady)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, pady = ppady)

point = Button(calc, text = ".")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 0, pady = ppady)

add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3, pady = ppady)

# Смена знака на противоположный
neg= Button(calc, text = "+/-")
neg["command"] = sum1.sign
neg.grid(row = 5, column = 0, pady = ppady)

# Очистка строки        
clear = Button(calc, text = "C")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = ppady)

# Очистка всего
all_clear = Button(calc, text = "AC")
all_clear["command"] = sum1.all_cancel
all_clear.grid(row = 5, column = 2, pady = ppady)

equals = Button(calc, text = "=")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = ppady)

root.mainloop()