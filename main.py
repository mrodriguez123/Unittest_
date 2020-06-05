#addition
def add(x,y):
    return x + y

#multiplication
def mult(x,y):
    return x * y

#division
def div(x,y):
    if y == 0:
        raise ValueError("Cannot have 0 as denominator")
    return x / y
    
#exponents
def exp(x,y):
    return x ** y

