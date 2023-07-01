#to find the values using inverse trigo functions
def sin_inv(x):
    if x==0:
        return 0
    elif x==0.5:
        return ("30,π/6")
    elif x==1/(2)**0.5:
        return ("45,π/4")
    elif x==(3)**0.5/2:
        return ("60,π/3")
    else:
        return ("90,π/2")
def cos_inv(x):
    if x==1:
        return 0
    elif x==(3)**0.5/2:
        return ("30,π/6")
    elif x==1/(2)**0.5:
        return ("45,π/4")
    elif x==0.5:
        return ("60,π/3")
    else:
        return ("90,π/2")

def tan_inv(x):
    if x==0:
        return 0
    elif x==1/(3)**0.5:
        return ("30,π/6")
    elif x==1:
        return ("45,π/4")
    elif x==(3)**0.5:
        return ("60,π/3")
    else:
        return ("90,π/2")



    
