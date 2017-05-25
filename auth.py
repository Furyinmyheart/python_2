__author__ = 'Андриченко Михаил Васильевич'

import tkinter
from tkinter import *
from hw_04_programm import *
from hw_04_defs import *

my_conn = Get_connect_to_db(host="localhost", database="my_scheme_py",
                                    user="root", password="Flammable1941")

def auth():

    def check_log_pass():
        my_conn = Get_connect_to_db(host="localhost", database="my_scheme_py",
                                    user=login.get(), password=password.get())

        sql_login = 'SELECT login FROM users WHERE id=1'
        sql_password = 'SELECT password FROM users WHERE id=1'
        try:
            if login.get() == str(sql_login) and password.get() == str(sql_password):
                pass
        finally: auth()

    root = Tk()
    root.title("Аутентификация")
    root.minsize(350,150)

    root.resizable(width=False, height=False)
    entry_pack = Frame(root)
    label_pack = Frame(root)

    bottom_pack = Frame(root)
    login = Entry(entry_pack, width=15)
    login.pack(side='top')
    label_login = Label(label_pack, text="Логин")

    label_login.pack(side='top')
    password = Entry(entry_pack, width=15)
    password.pack(side='top')
    label_password = Label(label_pack, text="Пароль")
    label_password.pack(side='top')
    
    butt = Button(bottom_pack, text="Войти", bg="white", fg="black", width=15, height=1, command=check_log_pass)

    butt.pack(side='top')
    entry_pack.pack(side='right')
    label_pack.pack(side='left')
    bottom_pack.pack(side='bottom')

    root.mainloop()
