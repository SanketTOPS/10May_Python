import re

#Sanket2020
usernm=input("Enter an username:")

usernm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(usernm_pattern,usernm)

if x: #true
    print("Username is valid!")
else:
    print("Error!Invalid Username")