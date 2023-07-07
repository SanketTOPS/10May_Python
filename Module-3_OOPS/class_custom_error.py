class student:
    a=0
    b=0
    def getsum(self):
        try:
            self.a=int(input("Enter A:"))
            self.b=int(input("Enter B:"))
            print("Sum:",self.a+self.b)
        except:
            raise Exception("Something went wrong...")
        

st=student()
st.getsum()
