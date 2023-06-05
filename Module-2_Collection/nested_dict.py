stdata={'st1':{'id':1,'name':'sanket','sub':'python'},'st2':{'id':2,'name':'mitesh','sub':'java'}}
"""print(stdata)
print(stdata['st1'])
print(stdata['st1']['sub'])"""


"""for i in stdata.values():
    print(i)"""

for i in stdata.values():
    print(i['name'])