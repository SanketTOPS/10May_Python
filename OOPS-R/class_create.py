class student:
    stid=12
    stnm='Nirav'

    def myfunc(self):
        print("This is student class.")
    

#object of class
st=student()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
