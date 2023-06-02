data=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter your data:")
    data.append(x)

print(tuple(data))

print(type(data))