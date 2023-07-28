import re

email=input("Enter an email:")

#sanket2020@gmail.com
email_pattern="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]{2,}$"

x=re.findall(email_pattern,email)

if x:
    print("Email is valid!")
else:
    print("Error!Invalid Email")