import sqlite3
import os
import hashlib


class Database(object):
    def __init__(self):
        self.path = 'app/storage'
        if not os.path.exists(os.path.join(self.path, 'db.sqlite')):
            conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))
            cur = conn.cursor()
            sql = '''
            create table for task
            '''
            sql1 = 'CREATE TABLE users(id integer primary key, name text not null, password text not null)'

            cur.execute(sql)
            cur.execute(sql1)

    def db_connect(self):
        conn = sqlite3.connect(os.path.join(self.path, 'db.sqlite'))
        return conn

    def create_table(self):
        conn = self.db_connect()
        cur = conn.cursor()
        cur.execute('CREATE TABLE tasks1(id integer primary key,rooms text not null,checkin text not null,date1 text not null,checkout text not null,date2 text not null,room_type text not null,NumOfAdults text , NumOfChild text)')
    def auth_user(self,user:tuple):
        conn = self.db_connect()
        cur = conn.cursor()
        sql = 'SELECT *FROM users WHERE name=?'
        name,passw = user
        try:
            pwd = hashlib.sha256(passw.encode()).hexdigest()
            userx = (name, pwd)
            cur.execute(sql, [name])
            conn.commit()
            dat = cur.fetchall()
            if len(dat)>0:
                db_user = dat[0]
                if pwd == db_user[2]:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)
            return []
    def add_user(self, user: tuple):
        conn = self.db_connect()
        cur = conn.cursor()
        name, passw = user
        try:
            pwd = hashlib.sha256(passw.encode()).hexdigest()
            userx = (name, pwd)

            sql = 'INSERT INTO users(name,password) VALUES(?,?)'
            cur.execute(sql, userx)
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def get_user(self):
        conn = self.db_connect()
        cur = conn.cursor()
        try:
            sql = 'SELECT *FROM users'
            cur.execute(sql)
            conn.commit()
            data = cur.fetchall()
            return data
        except Exception as e:
            print(e)
            return False

    def add_task(self, task: tuple):
        conn = self.db_connect()
        cur = conn.cursor()
        try:
            sql = 'INSERT INTO tasks1(rooms,checkin,date1,checkout,date2,room_type,NumOfAdults,NumOfChild) VALUES(?,?,?,?,?,?,?,?)'
            cur.execute(sql, task)
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False


    def update_task(self, task: list):
        conn = self.db_connect()
        cur = conn.cursor()
        try:
            sql = ''' UPDATE tasks1
            SET rooms=?,
            checkin=?,
            date1=?,
            checkout=?,
            date2=?,
            room_type=?,
            NumOfAdults=?,
            NumOfChild=?
            WHERE rooms=?
            '''
            # task.append(task[0])
            cur.execute(sql, task)
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_task(self, rooms):
        conn = self.db_connect()
        cur = conn.cursor()
        try:
            sql = '''
            DELETE FROM
            tasks1 WHERE rooms=?
            '''
            cur.execute(sql, [rooms])
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_task(self):
        conn = self.db_connect()
        cur = conn.cursor()
        try:
            sql = 'SELECT *FROM tasks1'
            cur.execute(sql)
            conn.commit()
            data = cur.fetchall()
            return data
        except Exception as e:
            print(e)
            return False
