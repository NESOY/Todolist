from src.Database import Database
import os.path

def test_createDatabase():
    # given
    name = "todolist_test.db"
    database = Database()
    # when
    database.createDatabase(name)
    # then
    assert os.path.exists(name) == True
    database.removeDatabase(name)

def test_removeDatabase():
    # given
    name = "todolist_test.db"
    database = Database()
    database.createDatabase(name)
    assert os.path.exists(name) == True
    # when
    database.removeDatabase(name)
    # then
    assert os.path.exists(name) == False