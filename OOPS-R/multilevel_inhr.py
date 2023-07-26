class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class nirav(ashok):
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")
    
class tops(nirav):
    def printdata(self):
        print("---------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("---------Nirav's Data--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
    
tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.printdata()