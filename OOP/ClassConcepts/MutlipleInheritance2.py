class TeamMemeber:
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid
    def display(self):
        print(f"Team Member:{self.name},UID:{self.uid}")

class Worker:
    def __init__(self,pay,jobTitle):
        self.pay = pay
        self.jobTitle = jobTitle
    def display(self):
        print(f"Worker:{self.jobTitle},Pay:{self.pay}")

class TeamLeader(Worker,TeamMemeber):
    def __init__(self, name, uid,pay,jobTitle,exper):
        self.exper = exper
        super().__init__(name,uid)
        Worker.__init__(self,pay,jobTitle)
    
    def display(self):
        super().display()
        print(f"Experience:{self.exper}")


tl = TeamLeader('Jake',1001,10000,'lead',10)
tl.display()
    
