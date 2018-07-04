import sqlite3 as sqlite
import sys

def init():
    conn = sqlite.connect("todolist.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS task(description TEXT)")

def add(param):
    conn = sqlite.connect("todolist.db")	
    with conn:
        cur = conn.cursor()
        sql = "INSERT INTO task(description) values (?)"
        cur.execute(sql, [param])
        conn.commit()

def list():
    conn = sqlite.connect("todolist.db")
    with conn:
        cur = conn.cursor()
        sql = "SELECT * FROM task"
        cur.execute(sql)
        print(cur.fetchall())

def main():
    command = input()
    tokens = command.split()
    init()
    if(tokens[1] == "add"):
        add(tokens[2])
    if(tokens[1] == "list"):
        list()

if __name__ == "__main__":
	main()
