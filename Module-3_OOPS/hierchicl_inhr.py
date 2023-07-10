class tops:
    cid=0
    cname=""

    def getdata(self):
        self.cid=input("Enter course id:")
        self.cname=input("Enter course name:")

class rohit(tops):
    def r_printdata(self):
        print("R_ID:",self.cid)
        print("R_Course Name:",self.cname)

class parth(tops):
    def p_printdata(self):
        print("P_ID:",self.cid)
        print("P_Course Name:",self.cname)

rh=rohit()
pr=parth()

rh.getdata()
rh.r_printdata()

pr.getdata()
pr.p_printdata()