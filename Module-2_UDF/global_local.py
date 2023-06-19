#global
"""a=34
b=65

def production():
    #local
    a=30
    b=30
    print("Mul:",a*b)

production()
print("Sum:",a+b)"""


# -------------- Global Keywords ---------------
a=12
print("A:",a)


def getA():
    global a
    a=68
    print("A:",a)

getA()
