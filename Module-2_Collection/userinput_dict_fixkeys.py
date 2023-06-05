stdata={}

keys=['id','name','sub']

for i in range(len(keys)):
    value=input(f"Enter your value for {keys[i]}:")

    stdata[keys[i]]=value

print(stdata)