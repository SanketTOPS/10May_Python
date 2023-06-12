def myfunc(id,name,sub):
    print("your id:",id)
    print("your name:",name)
    print("your sub:",sub)


for i in range(3):
    id = int(input("Enter your id : "))
    name = input("Enter your name : ")
    sub = input("Enter your sub : ")

    myfunc(id,name,sub)