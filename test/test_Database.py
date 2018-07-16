from src.Database import Database
import os.path

databaseName = "todolist_test.db"
tableName = "todo"
database = Database()

def setup_function(function):
    database.createDatabase(databaseName)
    database.createTable(tableName)

def teardown_function(function):
    database.removeDatabase(databaseName)



def test_createDatabase():
    database.createDatabase(databaseName)
    assert os.path.exists(databaseName) == True

def test_removeDatabase():
    database.createDatabase(databaseName)
    assert os.path.exists(databaseName) == True

    database.removeDatabase(databaseName)
    assert os.path.exists(databaseName) == False


def test_insertTodo():
    database.insertTodo("TODO", "CONTENT")
    todoList = database.getTodoList("TODO")
    assert len(todoList) == 1
    assert todoList[0][1] == "TODO"
    assert todoList[0][2] == "CONTENT"

def test_getTodoList():
    database.insertTodo("TODO", "CONTENT")
    todoList = database.getTodoList("TODO")
    assert len(todoList) == 1
    assert todoList[0][1] == "TODO"
    assert todoList[0][2] == "CONTENT"

    database.insertTodo("DOING", "CONTENT")
    todoList = database.getTodoList("DOING")
    assert len(todoList) == 1
    assert todoList[0][1] == "DOING"
    assert todoList[0][2] == "CONTENT"

    database.insertTodo("DONE", "CONTENT")
    todoList = database.getTodoList("DONE")
    assert len(todoList) == 1
    assert todoList[0][1] == "DONE"
    assert todoList[0][2] == "CONTENT"

def test_updateStatus():
    database.insertTodo("TODO", "CONTENT")
    todoList = database.getTodoList("TODO")
    assert len(todoList) == 1
    
    index = todoList[0][0]
    database.updateStatus(index, "DOING")
    todoList = database.getTodoList("DOING")
    assert len(todoList) == 1