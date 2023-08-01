from lib.make_snippet import *

def test_create_snippet():
    assert make_snippet("ciao") == "ciao"

def test_check_snippet():
    assert make_snippet("hello there") == "hello there..."
