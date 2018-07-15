import sqlite3 as sqlite


# SQL
SQL_GET_LIST = "SELECT * FROM task WHERE status = (?)"
SQL_DELETE_TODO = "DELETE FROM task WHERE id=(?)"

SQL_UPDATE_TODO = "UPDATE task SET status = (?) WHERE id=(?)"
SQL_UPDATE_START_TIME = "UPDATE task SET startTime = (?) WHERE id=(?)"
SQL_UPDATE_END_TIME = "UPDATE task SET endTime = (?) WHERE tid=(?)"

SQL_INSERT_TODO = "INSERT INTO task(status, description) values (?,?)"
SQL_CREATE_TABLE = "CREATE TABLE IF NOT EXISTS task(id INTEGER PRIMARY KEY, status TEXT, description TEXT, startTime TEXT, endTime TEXT)"
SQL_USED_TIME = "SELECT strftime('%s','now', 'localtime') - strftime('%s',(?));"

class Database:
    conn = None

    def createDatabase(databaseName):
        conn = sqlite.connect(databaseName)

    def createTable(tableName):
        with conn:
            cur = conn.cursor()
            cur.execute(databaseName)