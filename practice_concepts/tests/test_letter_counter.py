from lib.letter_counter import *

def test_letter_counter():
    program = LetterCounter("Digital Punk")
    result = program.calculate_most_common()
    assert result == [2, "i"]