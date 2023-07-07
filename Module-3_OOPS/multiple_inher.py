class rohit:
    rid=0
    rsub=''

    def r_getdata(self):
        self.rid=input("Enter Rohit's ID:")
        self.rsub=input("Enter Rohit's Subject:")

class parth:
    pid=0
    psub=''

    def p_getdata(self):
        self.pid=input("Enter Parth's ID:")
        self.psub=input("Enter Parth's Subject:")

class tops(rohit,parth):
    def printdata(self):
        print("----------Rohit's Data---------")
        print("Rohit's ID:",self.rid)
        print("Rohit's Subject:",self.rsub)
        print("----------Parth's Data---------")
        print("Parth's ID:",self.pid)
        print("Parth's Subject:",self.psub)

tp=tops()
tp.r_getdata()
tp.p_getdata()
tp.printdata()