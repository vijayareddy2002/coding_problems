from datetime import datetime
class Machine:
    def __init__(self,val1,val2,val3,val4):
        self.id=int(val1)
        self.mtype=val2
        self.timeused=int(val3)
        self.dateused=val4
class Machinemanager:
    def __init__(self,*args):
        self.machinelist=args[0]
    def assignMachine(self,machinename,d):
        l=[]
        co=[]
        date=[]
        d1=datetime.strptime(d,"%d/%m/%y")
        for i in self.machinelist:
            if(i.mtype==machinename):
                    d2=datetime.strptime(i.dateused,"%d/%m/%y")
                    delta=abs(d2-d1)
                    date.append(delta.days)
                    co.append(i.timeused)
                    l.append(i)
        k=min(co)
        print(k)
        z=co.index(k)
        print(z)
        if(date[z]>60):
            l[z].timeused=l[z].timeused+1
            l[z].dateused=d
            return [l[z].id,l[z].mtype,l[z].timeused]
        else:
            return []
    def getMachinesBytype(self):
        namecount={}
        for obj in self.machinelist :
            if obj.mtype in namecount:
                namecount[obj.mtype] += 1
            else :
                namecount[obj.mtype] = 1
        namecount=sorted(namecount.items(),key=lambda x:x[1])
        return namecount
if __name__ == "__main__" :
    print("enter no of objects")
    n=int(input())
    mlist=[]
    for i in range(n):
        val1=int(input())
        val2=input().upper()
        val3=int(input())
        val4=input()
        mobj=Machine(val1,val2,val3,val4)
        mlist.append(mobj)
    manageobj=Machinemanager(mlist)
    print("enter string")
    x=input().upper()
    print("enter date")
    v=input()
    rslt=manageobj.assignMachine(x,v)
    if len(rslt):
        print(rslt[0]," ",rslt[1]," ",rslt[2])
    else:
        print("no possible machine")
    func2=manageobj.getMachinesBytype()
    for i in func2:
        print(i)


        
