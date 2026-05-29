class TeamMemeber:
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid

class Worker:
    def __init__(self,pay,jobTitle):
        self.pay = pay
        self.jobTitle = jobTitle

class TeamLeader(Worker,TeamMemeber):
    def __init__(self, name, uid,pay,jobTitle,exper):
        self.exper = exper
        TeamMemeber.__init__(self,name,uid)
        Worker.__init__(self,pay,jobTitle)

        print("Name:{},uid:{},pay:{},jobTitle:{},Exp:{}".format(self.name,self.uid,self.pay,self.jobTitle,self.exper))

tl = TeamLeader('Jake',1001,10000,'lead',10)

print(TeamLeader.mro())
    
