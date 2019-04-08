import pymysql


class MySqlHelper():
    def __init__(self, _database):
        self.con =  None
        self.cursor = None
        self._database = _database
