s1=int(input("enter sub number:"))
s2=int(input("enter sub number:"))
s3=int(input("enter sub number:"))
s4=int(input("enter sub number:"))

total=s1+s2+s3+s4
pr=total/4
print("total",total)
print("pr",pr)

if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    if pr>70:
        print("dis..")
    elif pr>60:
        print("first class..")
    elif pr>50:
        print("second class.")
    elif pr>40:
        print("third class.")
else:
    print("fail")
        
    