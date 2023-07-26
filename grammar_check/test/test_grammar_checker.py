from lib.grammar_checker import *

def test_grammar_checker():
    tester = grammar_check("Hello!")
    assert tester == "grammar ok"

    tester = grammar_check("hello!")
    assert tester == "failed capital letters"

    tester = grammar_check("Hello")
    assert tester == "failed punctuation"

def test_grammar_errors():
    tester = grammar_check(2)
    assert tester == "enter a valid string"