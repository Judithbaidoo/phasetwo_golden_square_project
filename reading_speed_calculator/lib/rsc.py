# Calculate how long it takes for a user to read a texts noting that they can read 200 words a minute

def rsc(string):    #argument data type : string
    try:
        output = string.split()
        output = len(output)
        result = output / 200
        return result # datatype : float ; output : how many minutes it will take
    except(TypeError, AttributeError):
        return "enter a valid string"
