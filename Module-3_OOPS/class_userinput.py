class student:
    stid:int
    stnm:str

    def getdata(self):
        self.stid=input("Enter an ID:")
        self.stnm=input("Enter a Name:")
    
    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

st=student()
st.getdata()
st.printdata()

