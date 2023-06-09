def getdata(id,name,sub='Python'):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)


#getdata(101,'Sanket')
#getdata(101,'Sanket','JAVA')

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")

#getdata(stid,stnm)
#getdata(stid,stnm,stsub) #postional arguments

getdata(id=stid,name=stnm) #keywords argumnets

