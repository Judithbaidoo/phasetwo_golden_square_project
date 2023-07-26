# verify the grammar of a string by checking that it starts with a capital letter and that it has the correct punctuation

def grammar_check(string): # argument is a string
    try:
        first_char = string[0]
        last_char = string[-1]
        special_char = "!?."
        if first_char.isupper():
            if last_char in special_char:
                return "grammar ok"
            else:
                return "failed punctuation"
        else:
            return "failed capital letters"
    except(TypeError, AttributeError):
        return "enter a valid string"
        

# if it passes the tests it returns "grammar ok", if it fails for capital letters it returns "failed capital letters" , if it fails punctuation it returns "failed punctuation"

