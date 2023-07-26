# check that the string given includes the word TODO

def todo_checker(string): #datatype : string, I will put a string that contains TODO
    if string is None:
        return "enter a valid string"
    try:
        word = "#TODO"
        if word in string:
            return True
        else:
            return False
    except(AttributeError, TypeError):
        return "enter a valid string"
    
# it will return a boolean value , if empty or wrong datatype it will return "enter valid string"
