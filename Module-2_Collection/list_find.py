data=['ahmedabad','surat','navsari','baroda','rajkot','mumbai','delhi']

print(data)

newlist=[]

for i in data:
    if 'e' in i:
        newlist.append(i)

print(newlist)
