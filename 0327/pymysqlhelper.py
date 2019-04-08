"""
MYSQL 辅助类：减少和数据库交互代码编写量
"""
import pymysql


class MySqlHelper():
    def __init__(self, _database="goods", _user="root", _password="123456", _host="localhost", _port=3306, _charset="utf8"):
        self.con = None
        self.cursor = None
        try:
            self.con = pymysql.Connect(host=_host, user=_user, password=_password,
                                       database=_database, port=_port, charset=_charset)
            self.cursor = self.con.cursor()

        except Exception as e:
            print(e)

    def select_db(self, dbname):
        self.con.select_db(dbname)

    def queryone(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self._close()

    def querymany(self, sql, n, args=None):
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchmany(n)
        except Exception as e:
            print(e)
        finally:
            self._close()

    def queryall(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self._close()

    def update(self, sql, args=None):
        try:
            row = self.cursor.execute(sql, args)
            self.con.commit()
            return row
        except Exception as e:
            self.con.rollback()
            print(e)
        finally:
            self._close()

    def _close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.con is not None:
            self.con.close()
