class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)


class otherstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)


st=student()
ot=otherstudent()

st.getdata(1,'Sanket')
ot.getdata(2,'Mitesh')