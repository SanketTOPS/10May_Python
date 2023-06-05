stdata={'id':101,'name':'sanket','sub':'python'}
"""print(stdata)
print(stdata['sub'])
print(stdata.get('id'))
print(stdata.keys())
print(stdata.values())
print(len(stdata))"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


"""print(stdata)
stdata['id']=102
print(stdata)"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

#print(stdata)
#stdata['city']='rajkot'
#stdata.pop('sub')
#stdata.popitem()
#stdata.clear()
#del stdata
print(stdata)   


newdict=stdata.copy()
print(newdict)