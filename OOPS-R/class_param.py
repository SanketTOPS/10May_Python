class student:
    def getdata(sanket,id,name):
        print("ID:",id)
        print("Name:",name)
    
st=student() #object
#st.getdata(101,'Sanket')
stid=input("Enter ID:")
stnm=input("Enter Name:")
st.getdata(id=stid,name=stnm)