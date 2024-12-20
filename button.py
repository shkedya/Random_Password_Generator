import string
from tkinter import *
import random


master = Tk()
master.title('Random Password Generator!')
Label(master, text="Select the checkboxes for what you want your password to contain\n Regular letters are "
                   "automatically included").grid(row=0, sticky=W)
var0 = StringVar()
new_label = Label(master, textvariable=var0).grid(row=1, sticky=W)
var0.set("Click a number to determine how many characters your password will have: ")


def change_color1():
    """Switches button 1 color"""
    button1.configure(bg='#20b2aa')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color2():
    """Switches button 2 color"""
    button1.configure(bg='white')
    button2.configure(bg='#20b2aa')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color3():
    """Switches button 3 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='#20b2aa')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color4():
    """Switches button 4 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='#20b2aa')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color5():
    """Switches button 5 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='#20b2aa')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color6():
    """Switches button 6 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='#20b2aa')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color7():
    """Switches button 7 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='#20b2aa')
    button8.configure(bg='white')
    button9.configure(bg='white')


def change_color8():
    """Switches button 8 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='#20b2aa')
    button9.configure(bg='white')


def change_color9():
    """Switches button 9 color"""
    button1.configure(bg='white')
    button2.configure(bg='white')
    button3.configure(bg='white')
    button4.configure(bg='white')
    button5.configure(bg='white')
    button6.configure(bg='white')
    button7.configure(bg='white')
    button8.configure(bg='white')
    button9.configure(bg='#20b2aa')


button1 = Button(master, text="1", padx=10, pady=5, bg='#20b2aa', command=change_color1)
button1.grid(row=1, column=1)
button2 = Button(master, text="2", padx=10, pady=5, bg='white', command=change_color2)
button2.grid(row=1, column=2)
button3 = Button(master, text="3", padx=10, pady=5, bg='white', command=change_color3)
button3.grid(row=1, column=3)
button4 = Button(master, text="4", padx=10, pady=5, bg='white', command=change_color4)
button4.grid(row=1, column=4)
button5 = Button(master, text="5", padx=10, pady=5, bg='white', command=change_color5)
button5.grid(row=1, column=5)
button6 = Button(master, text="6", padx=10, pady=5, bg='white', command=change_color6)
button6.grid(row=1, column=6)
button7 = Button(master, text="7", padx=10, pady=5, bg='white', command=change_color7)
button7.grid(row=1, column=7)
button8 = Button(master, text="8", padx=10, pady=5, bg='white', command=change_color8)
button8.grid(row=1, column=8)
button9 = Button(master, text="9", padx=10, pady=5, bg='white', command=change_color9)
button9.grid(row=1, column=9)
var1 = IntVar()
Checkbutton(master, text="Capital Characters", variable=var1).grid(row=3, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Special Characters", variable=var2).grid(row=4, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Numbers", variable=var3).grid(row=5, sticky=W)
Button(master, text='Generate Password', command=master.quit).grid(row=6, sticky=W, pady=4)
mainloop()


class Data:
    """
    Represents the buttons' data
    """
    def __init__(self):
        self.characters = string.ascii_lowercase
        self.capitals = string.ascii_uppercase
        self.specials = string.punctuation
        self.list_nums = string.digits
        self.length_password = 1
        self.temp_var = string.ascii_lowercase

    def password_length(self):
        if button1['bg'] == '#20b2aa':
            self.length_password = 1
        if button2['bg'] == '#20b2aa':
            self.length_password = 2
        if button3['bg'] == '#20b2aa':
            self.length_password = 3
        if button4['bg'] == '#20b2aa':
            self.length_password = 4
        if button5['bg'] == '#20b2aa':
            self.length_password = 5
        if button6['bg'] == '#20b2aa':
            self.length_password = 6
        if button7['bg'] == '#20b2aa':
            self.length_password = 7
        if button8['bg'] == '#20b2aa':
            self.length_password = 8
        if button9['bg'] == '#20b2aa':
            self.length_password = 9
        return self.length_password
    
    def get_temp_var(self):
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
            self.temp_var = self.characters + self.capitals
        if var1.get() == 0 and var2.get() == 1 and var3.get() == 0:
            self.temp_var = self.characters + self.specials
        if var1.get() == 0 and var2.get() == 0 and var3.get() == 1:
            self.temp_var = self.characters + self.list_nums
        if var1.get() == 1 and var2.get() == 1 and var3.get() == 0:
            self.temp_var = self.characters + self.capitals + self.specials
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 1:
            self.temp_var = self.characters + self.capitals + self.list_nums
        if var1.get() == 0 and var2.get() == 1 and var3.get() == 1:
            self.temp_var = self.characters + self.specials + self.list_nums
        if var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
            self.temp_var = self.characters + self.capitals + self.specials + self.list_nums
        if var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
            return self.temp_var
        return self.temp_var


the_data = Data()
new_choice = random.sample(the_data.get_temp_var(), the_data.password_length())
new_password = "".join(new_choice)
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, new_password)
wb.save('password_data.xls')
