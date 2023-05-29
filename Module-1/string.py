mystr="This is Python!"

print(mystr)
print(mystr[0])
print(mystr[-1])
print(mystr[0:4]) #slice (range)
print(mystr[5:])
print(mystr[:8])

print(len(mystr))


if 'This' in mystr:
    print("Yes..")
else:
    print("Noo")