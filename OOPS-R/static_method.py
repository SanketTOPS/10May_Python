class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("ID:",student.stid)
        print("Name:",student.stnm)

    @staticmethod
    def getsum(a,b):
        print("Sum:",a+b)

st=student()
st.getdata()
st.getsum(23,45)