data=['html','python','java','c++','react']
#print(data)
"""print(data[0])
print(data[-1])
print(data[0:3])
print(data[2:])
print(data[:4])
print(len(data))"""
#data[0]='android'


"""if 'java' in data:
    print("Yes...")
else:
    print("No")"""

#print(data.index('c++'))

"""for i in data:
    #print(i)
    print(f"{i}={data.index(i)}")"""

"""n=0
for i in data:
    print(f"{i}={n}")
    n+=1"""

#data.append('angular')
#data.insert(2,'iOS')
#data.pop()
#data.pop(2)
#data.remove('c++')
#data.clear()
#del data[0]
#del data
#data.sort()
#data.reverse()
#print(data)

#newlist=["HTML5","CSS3","JS"]
#print(newlist)
#print(data+newlist)
#data.extend(newlist)
#print(data)


#newlist=data.copy()
#print(newlist)

# ------------------------------------ #
print(data)

newlist=("HTML5","CSS3","JS")
data.extend(newlist)
print(data)