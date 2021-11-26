def catAndMouse(x, y, z):
    c1=abs(z-x)
    c2=abs(y-z)
    if(c1==c2):
        return "Mouse C"
    elif(c1<c2):
        return "Cat A"
    else:
        return "Cat B"
