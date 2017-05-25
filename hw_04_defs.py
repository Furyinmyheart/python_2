__author__ = 'Андриченко Михаил Васильевич'

import sys
import mysql.connector
from mysql.connector import MySQLConnection, Error
import threading

__name__ == '__main__'

class Artificial_intelligence:

    def __init__(self, id, name, developer):
        self._id = id
        self._name = name
        self._developer = developer

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, value):
        self._developer = value

    def __str__(self):
        return 'ID ИИ: {}, наименование : {}, разработчик: {}'.format(self._id, self._name, self._developer)


class Human_ai(Artificial_intelligence):

    def __init__(self, id, name, developer, gender, age):
        super().__init__(id, name, developer)
        self._gender = gender
        self._age = age


    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return super().__str__() + ', пол: {}, возраст: {},'.format(self._gender, self._age)

class Artificial_network:

    def __init__(self, count_users):
        self._ai_network = []
        self._count_users = count_users

    @property
    def count_users (self):
        return self._count_users

    def add_user (self, new_user):
        if len(self._ai_network) < self._count_users:
            self._ai_network.append(new_user)

    def __len__(self):
        return len(self._ai_network)

    def get_user(self, id):
        get_user = list(filter(lambda user: user.id == id, self._ai_network))
        return get_user[0] if len(get_user) == 1 else None

    def __str__(self):
        return '\n'.join(map(str, self._ai_network))

class Get_connect_to_db:
    host = 'localhost'
    database = 'my_scheme_py'
    user = 'root'
    password = 'Flammable1941'

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        try:
            conn = mysql.connector.connect(host = host,
                                       database = database,
                                       user = user,
                                       password = password)
            if conn.is_connected():
                pass
#                print('Вы успешно подключились к базе данных MySQL.')
        except Error as e:
            print(e)

    def stop_con(self):
        conn = mysql.connector.connect(host = self.host,
                                       database = self.database,
                                       user = self.user,
                                       password = self.password)
        conn.close()

    def aft(self, login_t, password_t):
        try:
            sql = "SELECT role FROM users WHERE login = %s and password = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, (login_t, password_t))
            rows = c.fetchall()
            if (rows == []):
                rows = ['e', 'r', 'r', 'o', 'r']
            return rows[0]
        except Error as e:
            return e

    def add_ai(self, id, name, developer, gender, age):
        try:
            sql = "INSERT INTO Artificial_network (_ID, _NAME)" \
                     " VALUES(%s, %s)"
            sql_ai = "INSERT INTO Artificial_intelligence(_ID, _NAME, _DEVELOPER)" \
                     " VALUES(%s,%s,%s)"
            sql_human_ai = "INSERT INTO Human_ai(_ID, _NAME, _DEVELOPER, _GENDER, _AGE)" \
                  " VALUES(%s,%s,%s,%s,%s)"

            args = (id, name)
            args_ai = (id, name, developer, )
            args_human_ai = (id, name, developer, gender, age)
            conn = mysql.connector.connect(host = self.host,
                                           database = self.database,
                                           user = self.user,
                                           password = self.password)
            c = conn.cursor()
            c.execute(sql, args)
            c.execute(sql_ai, args_ai)
            c.execute(sql_human_ai, args_human_ai)
            conn.commit()

        except Error as e:
            print(e)

    def update_name_ai(self, name, id):
        try:
            sql = "UPDATE artificial_network SET _NAME = %s WHERE _id = %s"
            sql_ai = "UPDATE artificial_intelligence SET _NAME = %s WHERE _id = %s"
            sql_human_ai = "UPDATE human_ai SET _NAME = %s WHERE _id = %s"

            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)

            c = conn.cursor()
            c.execute(sql, (name, id))
            c.execute(sql_ai, (name, id))
            c.execute(sql_human_ai, (name, id))
            conn.commit()
        except Error as e:
            print(e)

    def delete_ai(self, id):
        try:
            sql = "DELETE FROM artificial_network WHERE _ID = %s"
            sql_ai = "DELETE FROM artificial_intelligence WHERE _ID = %s"
            sql_human_ai = "DELETE FROM human_ai WHERE _ID = %s"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql, (id,))
            c.execute(sql_ai, (id,))
            c.execute(sql_human_ai, (id,))
            conn.commit()
        except Error as e:
            print(e)

    def export_Developer(self):
        try:
            sql_Developer = "SELECT _DEVELOPER INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/" \
                            "Uploads/test_Dev.txt' FROM artificial_intelligence;"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql_Developer)
            conn.commit()
        except Error as e:
            print(e)

    def export_Name(self):
        try:
            sql_Name = "SELECT _NAME INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/" \
                            "Uploads/test_Name.txt' FROM artificial_intelligence;"
            conn = mysql.connector.connect(host=self.host,
                                           database=self.database,
                                           user=self.user,
                                           password=self.password)
            c = conn.cursor()
            c.execute(sql_Name)
            conn.commit()
        except Error as e:
            print(e)

    def print_ai(self):
        try:
            sql_ai = "SELECT _ID, _NAME, _DEVELOPER FROM artificial_intelligence"
            sql_human_ai = "SELECT _ID, _NAME, _DEVELOPER, _GENDER, _AGE FROM human_ai"
            conn = mysql.connector.connect(host=self.host,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password)
            c = conn.cursor()
            c.execute(sql_ai)
            #print('---------------------------------------------')
            #print("Список всех ИИ в базе artificial_intelligence")
            #print('---------------------------------------------')
            rows_1 = c.fetchall()
            c.execute(sql_human_ai)
            #print('------------------------------')
            #print("Список всех ИИ в базе human_ai")
            #print('------------------------------')
            rows_2 = c.fetchall()
            return (rows_1, "Список всех ИИ в базе artificial_intelligence", '\n', rows_2,
                    "Список всех ИИ в базе human_ai")
        except Error as e:
            print(e)

def quitnow():
    print('Работа программы завершена')
    sys.exit()

def my_menu():
    global my_conn
    print ('|-------------------------------------------------|')
    print ('|                      MENU                       |')
    print ('|-------------------------------------------------|')
    print ('|1. Подключиться к SQL серверу                    |')
    print ('|2. Добавить новый ИИ в базу данных               |')
    print ('|3. Изменить существующее имя ИИ по ID            |')
    print ('|4. Удалить данные ИИ из базы по ID               |')
    print ('|5. Вывести данные о хранящихся ИИ в базе на экран|')
    print ('|6. Завершить работу                              |')
    print ('|-------------------------------------------------|')
    key = input("Выберите пункт меню: ")
    for x in key:
        if key == '1':
            my_conn = Get_connect_to_db(host="localhost", database="my_scheme_py",
                                    user="root", password="Pass123")
            my_menu()
        if key == '2':
            id = input('Введите ID для ИИ: ', )
            name = input('Введите имя, используемое ИИ: ', )
            developer = input('Введите разработчика ИИ: ', )
            gender = input('Введите пол ИИ: ', )
            age = input('Введите возраст ИИ: ', )
            my_conn.add_ai(id, name, developer, gender, age)
            my_menu()
        if key == '3':
            id = input('Введите ID ИИ: ', )
            name = input('Введите новое имя для ИИ: ', )
            my_conn.update_name_ai(name,id)
            my_menu()
        if key == '4':
            id = input('Введите ID ИИ: ', )
            my_conn.delete_ai(id)
            my_menu()
        if key == '5':
            my_conn.print_ai()
        if key == '6':
            quitnow()
    else:
        my_menu()
