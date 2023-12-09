#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter as tk



# создаем класс ДЭС
class Gep():
    status = 0
    key = 0
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    # создаем вложенный класс параметров ДЭС
    class Param():
        def __init__(self, frame_gep, name, x, y):
            self.param_name = name
            self.u_min = 215
            self.u_max = 253
            self.f_min = 49.6
            self.f_max = 50.4
            self.t_min = 40
            self.t_max = 100
            self.p_min = 0.35
            self.p_max = 0.45

            lb = Label(frame_gep, text=self.param_name, width=7, font="serif 11", bg='orange', relief=RIDGE, borderwidth=2)
            lb.place(x = x, y = y)
            self.lb_value = Label(frame_gep, width=5, font="serif 11", relief=RIDGE, borderwidth=2)
            self.lb_value.place(x = x + 80, y = y)

        def set_value(self, value):
            self.lb_value.config(text=value)
            if self.param_name == 'Ua' or 'Ub' or 'Uc':
                if value <= self.u_min or value >= self.u_max:
                    self.lb_value.config(bg='red')
                else:
                    self.lb_value.config(bg='spring green')
            if self.param_name == 'F':
                if value <= self.f_min or value >= self.f_max:
                    self.lb_value.config(bg='red')
                else:
                    self.lb_value.config(bg='spring green')
            if self.param_name == 'T':
                if value <= self.t_min or value >= self.t_max:
                    self.lb_value.config(bg='red')
                else:
                    self.lb_value.config(bg='spring green')
            if self.param_name == 'P':
                if value <= self.p_min or value >= self.p_max:
                    self.lb_value.config(bg='red')
                else:
                    self.lb_value.config(bg='spring green')
            if Gep.status == 0:
                self.lb_value.config(bg='gray99')

    def creat(self):
        # загружаем картинку ДЭС
        self.image_gep = PhotoImage(file='gep.png')

        # создаем фрейм ДЭС
        self.frame_gep = Frame(frame_root, width=562, height=270, relief=GROOVE, borderwidth=2)
        self.frame_gep.place(x=self.x, y=self.y)

        # рисуем картинку ДЭС
        lb_image_gep = Label(self.frame_gep, image=self.image_gep, relief=RIDGE, borderwidth=2)
        lb_image_gep.place(x=5, y=10)

        # рисуем имя ДЭС
        lb_name_gep = Label(self.frame_gep, width=10, text=self.name, font="serif 16", bg='gray99', relief=RIDGE, borderwidth=2)
        lb_name_gep.place(x=30, y=164)

        # рисуем поле статуса ДЭС
        self.lb_status_gep = Label(self.frame_gep, width=14, font="serif 16", relief=RIDGE, borderwidth=2)
        self.lb_status_gep.place(x=180, y=164)

        # рисуем поле ошибок ДЭС
        self.lb_key_gep = Label(self.frame_gep, width=28, font="serif 16", relief=RIDGE, borderwidth=2)
        self.lb_key_gep.place(x=5, y=225)

        # рисуем поля параметров ДЭС
        self.Ua = Gep.Param(self.frame_gep, 'Ua', 420, 10)
        self.Ub = Gep.Param(self.frame_gep, 'Ub', 420, 40)
        self.Uc = Gep.Param(self.frame_gep, 'Uc', 420, 70)
        self.F = Gep.Param(self.frame_gep, 'F', 420, 100)
        self.T = Gep.Param(self.frame_gep, 'T', 420, 130)
        self.P = Gep.Param(self.frame_gep, 'P', 420, 160)

        # создаем кнопку ЗАПУСК
        bt_start = Button(self.frame_gep, text='ЗАПУСК', height=1, width=13, font="serif 10", command=root.destroy)
        bt_start.place(x=420, y=192)

        # создаем кнопку ОСТАНОВ
        bt_stop = Button(self.frame_gep, text='ОСТАНОВ', height=1, width=13, font="serif 10", command=root.destroy)
        bt_stop.place(x=420, y=227)

    # задаем статус ДЭС
    def set_status(self, status):
        self.status = status
        if self.status == 0:
            self.lb_status_gep.config(text='ОСТАНОВЛЕН', bg='gray99')
        if self.status == 1:
            self.lb_status_gep.config(text='РАБОТАЕТ', bg='spring green')
        Gep.status = self.status

    # задаем ошибки ДЭС
    def set_key(self, key):
        self.key = key
        if self.key == 0:
            self.lb_key_gep.config(text='РУЧНОЙ', bg='gray99')
        if self.key == 1:
            self.lb_key_gep.config(text='АВТОМАТИЧЕСКИЙ', bg='gray99')
        if self.key == 2:
            self.lb_key_gep.config(text='СЕРВИСНЫЙ', bg='gray99')
        Gep.key = self.key


root = Tk()
icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)
root.title('АСУ ДЭС')
root.geometry('1920x1080')
root.attributes('-fullscreen', True)
root.resizable(0, 0)

# создаем фрейм главного окна
frame_root = Frame(root, width = 1910, height = 1070, relief = GROOVE, borderwidth = 2)
frame_root.place(x = 5, y = 5)

# создаем надпись главного окна
lb_head = Label(frame_root, text='АВТОМАТИЗИРОВАННАЯ СИСТЕМА МОНИТОРИНГА ДИЗЕЛЬНЫХ ЭЛЕКТРОУСТАНОВОК', width=94, font="serif 24", anchor="center", relief=RIDGE, borderwidth=2)
lb_head.place(x=10, y=10)

# создаем кнопку ВЫХОД
bt_exit = Button(frame_root, text = 'ВЫХОД', height = 2, width = 10, font = "serif 10",	command = root.destroy)
bt_exit.place(x = 1789, y = 70)

# создаем таблицу журнала
frame_tree = Frame(frame_root, width = 1885, height = 155, relief = GROOVE, borderwidth = 2)
frame_tree.place(x = 10, y = 905)

columns = (('date', 200), ('time', 200), ('message', 1270), ('type', 200))
tree = ttk.Treeview(frame_tree, columns=[col[0] for col in columns], show = 'headings', height = 6)
tree.heading('date', text = 'Дата')
tree.heading('time', text = 'Время')
tree.heading('message', text = 'Событие')
tree.heading('type', text = 'Категория')
for col, width in columns:
    tree.column(col, width = width)
scrollbar = ttk.Scrollbar(frame_tree, orient = tk.VERTICAL, command = tree.yview)
tree.configure(yscroll = scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
tree.pack()


gep_100 = Gep(name = 'ДЭС 1', x = 10, y = 70)
gep_100.creat()
gep_100.set_status(1)
gep_100.Ua.set_value(220)
gep_100.Ub.set_value(280)
gep_100.Uc.set_value(215)
gep_100.F.set_value(50)
gep_100.T.set_value(100)
gep_100.P.set_value(0.42)

gep_200 = Gep(name = 'ДЭС 2', x = 10, y = 350)
gep_200.creat()
gep_200.set_status(0)
gep_200.Ua.set_value(0)
gep_200.Ub.set_value(0)
gep_200.Uc.set_value(0)
gep_200.F.set_value(0)
gep_200.T.set_value(40)
gep_200.P.set_value(0.35)

gep_300 = Gep(name = 'ДЭС 3', x = 10, y = 630)
gep_300.creat()
gep_300.set_status(0)
gep_300.Ua.set_value(0)
gep_300.Ub.set_value(0)
gep_300.Uc.set_value(0)
gep_300.F.set_value(0)
gep_300.T.set_value(3)
gep_300.P.set_value(0.00)

gep_200.set_key(0)
gep_300.set_key(2)
gep_100.set_key(1)

root.mainloop()