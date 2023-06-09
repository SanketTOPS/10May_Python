# WAP to get 4 sub marks and print total and pr and find the result. (Nested)

s1=int(input("enter subject mark 1:"))
s2=int(input("enter subject mark 2:"))
s3=int(input("enter subject mark 3:"))
s4=int(input("enter subject mark 4:"))

if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    
    total=s1+s2+s3+s4
    print("total",total)
    pr=total/4
    print("pr",pr)
    if pr>=70:
        print("your result is dist")
    elif pr>=60:
        print("your result is first class")
    elif pr>=50:
        print("your result is second class")
else:
    print("your result is FAIL")



