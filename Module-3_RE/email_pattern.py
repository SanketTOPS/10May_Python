import re

#sanket2020@gmail.com
email=input("Enter an email:")

email_pattern="^[a-z0-9_.]+[@]+[a-z]+[\.]+[a-z]{2,3}$"

x=re.findall(email_pattern,email)

if x: #true
    print("Email is valid!")
else:
    print("Error!Invalid Email")