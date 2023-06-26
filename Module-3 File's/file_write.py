file=open('test.txt','a')

#file.write("Good evening!")


"""if file.writable():
    print("Yes...Now you can write anything.")
else:
    print("Error!Change your file mode.")"""


n=int(input("Enter number of students:"))
    
for i in range(n):
    id=input("Enter ID:")
    name=input("Enter Name:")

    """file.write(id)
    file.write(name)"""

    file.write(f'ID:{id}\nName:{name}\n')
