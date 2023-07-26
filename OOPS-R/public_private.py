class student:
    #private
    __stid=1
    __stnm='Nirav'

    #private
    def __getdata(self):
        print("This is getdata!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    #public
    def prindata(self):
        self.__getdata()


st=student()
#print(st.stid)
#print(st.stnm)
#st.getdata()
st.prindata()