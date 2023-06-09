# WAP to store students data in dict.
# ID, name, sub, city

st_data1={}
st_data2={}

n=int(input("Enter number of main string : "))
key=['ID', 'name', 'sub', 'city']

for i in range(n):
    key1=input("Enter your main key : ")
    for j in range(len(key)):
        value=input(f"Enter value of {key[j]} : ")

        st_data2[key[j]]=value
        st_data1[key1]=st_data2.copy()

"""
my_list1=[i for i in st_data1]
print(my_list1)"""
my_list=list(st_data1.items())
print(my_list)