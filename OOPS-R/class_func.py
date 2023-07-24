class student:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is student class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)
    

st=student()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
st.getsum(34,56)