class student:
    x=0
    y=0
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def getsum(self):
        print("Sum:",self.x+self.y)
    
    def getmul(self):
        print("Mul:",self.x*self.y)


st=student(45,67)
st.getsum()
st.getmul()
        