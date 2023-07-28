import re

"""mystr="This is Python!"

x=re.findall('Py..on',mystr)
print(x)"""


mystr="This is Python!45364"

"""#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
x=re.findall('on$',mystr)
print(x)"""


#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\AThis',mystr)
#x=re.findall('43\Z',mystr)
#x=re.findall(r'\bThis',mystr)
#x=re.findall('\B48',mystr)
#x=re.findall('This|That',mystr)
x=re.findall('[A-Z]|[a-z]',mystr)
print(x)