class student:
    stid=23
    stname='Sanket'

    def myfunc(self):
        print("This is student class.")

# Object of class
st=student()
print(st.stid)
print(st.stname)

st.myfunc()