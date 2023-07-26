from lib.todo_checker import *

def test_todo_checker():
    checker = todo_checker("bvksdj#TODO")
    assert checker == True
    checker = todo_checker("bvksdj")
    assert checker == False

def test_todo_checker_errors():
    checker = todo_checker(4)
    assert checker == "enter a valid string"
    checker = todo_checker()
    assert checker == "enter a valid string"