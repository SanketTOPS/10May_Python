import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='testdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

# Create Table
create_tbl="create table topsdb(id integer primary key auto_increment, fname text, sub text)"
try:
    cr.execute(create_tbl)
    print("Table Created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo values(1,'sanket','python'),(2,'nirav','java'),(3,'mitesh','php'),(4,'ashok','angular'),(5,'hitesh','c++')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
#update_data="update studinfo set sub='HTML' where id=3"
"""update_data="update studinfo set name='pratik',sub='php' where id=4"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)
