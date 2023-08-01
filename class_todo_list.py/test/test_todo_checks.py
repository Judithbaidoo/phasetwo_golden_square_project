from lib.todo_challenge import *
from lib.todo import *

def test_add_item_on_list():
    todo_list = TodoList()
    #result = todo_list.add()

def test_initialise_as_false():
    todo = Todo("coding exercises")
    assert todo.completed == False
    assert todo.task == "coding exercises"

def test_initialise_as_true():
    todo = Todo("coding exercises")
    todo.mark_complete()
    assert todo.completed == True

def test_todo_false_instance():
    todolist = TodoList()
    entry1 = Todo("coding exercises")
    todolist.add(entry1)
    assert todolist.incomplete() == [entry1.task]

def test_todo_true_instance():
    todolist = TodoList()
    entry1 = Todo("coding exercises")
    entry2 = Todo("study")
    entry2.mark_complete()
    todolist.add(entry1)
    todolist.add(entry2)
    assert todolist.incomplete() == [entry1.task]

def test_mark_all_as_true():
    checklist = TodoList()
    entry1 = Todo("wash up")
    entry2 = Todo("sweep up")
    entry3 = Todo("go shops")
    checklist.add(entry1)
    checklist.add(entry2)
    checklist.add(entry3)
    entry1.mark_complete()
    checklist.give_up()
    assert checklist.complete() == [entry1.task,entry2.task,entry3.task]
