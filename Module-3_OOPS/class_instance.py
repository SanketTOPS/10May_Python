class student:
    stid=1
    stnm="Nirav"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)
    
# Using Object
"""st=student()
st.getdata()
st.stid=45
st.stnm="Ashok"
st.getdata()"""


# Instance
student().getdata()
student().stid=23
student().stnm="Mitesh"
student().getdata()