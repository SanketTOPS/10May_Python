class student:
    stid=1
    stnm='Ashok'

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object
"""st=student()
st.getdata()
st.stid=2
st.stnm='Sanket'
st.getdata()"""

#Instance
student().getdata()
student().stid=2
student().stnm='Nirav'
student().getdata()