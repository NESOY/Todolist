import sqlite3 as sqlite
import os.path

# SQL
## CREATE
SQL_CREATE_TABLE = "CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, status TEXT, content TEXT, startTime TEXT, endTime TEXT)"
SQL_INSERT_TODO = "INSERT INTO {}(status, content) values (?,?)"
SQL_GET_LIST = "SELECT * FROM {} WHERE status = (?)"
SQL_UPDATE_TODO = "UPDATE {} SET status = (?) WHERE id=(?)"

SQL_UPDATE_START_TIME = "UPDATE {} SET startTime = (?) WHERE id=(?)"
SQL_UPDATE_END_TIME = "UPDATE {} SET endTime = (?) WHERE tid=(?)"
SQL_USED_TIME = "SELECT strftime('%s','now', 'localtime') - strftime('%s',(?));"
SQL_DELETE_TODO = "DELETE FROM {} WHERE id=(?)"

class Database:
    conn = None
    databaseName = None
    tableName = None

    def createDatabase(self, databaseName):
        self.conn = sqlite.connect(databaseName)
        self.databaseName = databaseName

    def removeDatabase(self, databaseName):
        if os.path.exists(databaseName):
            os.remove(databaseName)
            self.databaseName = None

    def createTable(self, tableName):
        self.tableName = tableName
        SQL = SQL_CREATE_TABLE.format(tableName)
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(SQL)
    
    def insertTodo(self, status, content):
        SQL = SQL_INSERT_TODO.format(self.tableName)
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(SQL, [status, content])

    def getTodoList(self, status):
        SQL = SQL_GET_LIST.format(self.tableName)
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(SQL, [status])
            return cur.fetchall()

    def updateStatus(self, index, status):
        SQL = SQL_UPDATE_TODO.format(self.tableName)
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(SQL, [status, index])
            return cur.fetchall()