import sqlite3 as sqlite
import sys
def main():
    command = input()
    tokens = command.split()
    init()
    if(tokens[1] == "add"):
        add(tokens[2])

def init():
    conn = sqlite.connect("todolist.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS task(description TEXT)")
    print("Create Database")

def add(param):
    conn = sqlite.connect("todolist.db")	
    with conn:
        cur = conn.cursor()
        sql = "INSERT INTO task(description) values (?)"
        cur.execute(sql, [param])
        conn.commit()
    print("Success Save Task")



if __name__ == "__main__":
	main()
