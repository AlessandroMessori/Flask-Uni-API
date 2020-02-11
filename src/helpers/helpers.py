class DataHelper:

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

    def getFilteredData(self,propName,propValue):
        dat = list(self.data.find({propName:propValue}))
        
        if (len(dat) == 0):
            return []
        
        for elem in dat:
            del elem["_id"]

        return dat

    def addElement(self,data):
        try:
            self.data.insert(data)
        except():
            raise Exception(e)

    def updateElement(self,data):
        pass

    def deleteElement(self,propName,propValue):
        try:
            self.data.remove({propName:propValue})
        except:
            raise Exception()
        