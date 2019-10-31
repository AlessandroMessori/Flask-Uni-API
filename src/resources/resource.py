class Resource:

    def __init__(self,name,con):
        self.name = name
        self.con = con
        self.data = con[name]

    def getData(self):
        res = []
        for ent in list(self.data.find()):
            del ent["_id"]
            res.append(ent)
        return res
    
    def getSingleData(self,prop,id):
        dat = list(self.data.find({prop:id}))
        
        if (len(dat) == 0):
            return []
        
        del dat[0]["_id"]
        return dat[0]