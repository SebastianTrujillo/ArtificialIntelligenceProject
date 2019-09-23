#==============================================================================
#==================================Main Model==================================
#==============================================================================
class MainModel(object):

    def __init__(self,matrixSize=None,matrix=None):
        super(MainModel,self).__init__()
        self.matrixSize=matrixSize
        self.matrix=matrix
        self.startPosition=[]
        self.metaPosition=[]
        self.costPosition=[]

    def getMatrixSize(self):
        return(self.matrixSize)

    def getMatrix(self):
        return(self.matrix)

    def getStartPosition(self):
        self.startPosition=[]
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                if(self.matrix[i][j]=="S"):
                    self.startPosition.append(i)
                    self.startPosition.append(j)
        return(self.startPosition)

    def getMetaPosition(self):
        self.metaPosition=[]
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                if (self.matrix[i][j]=="M"):
                    self.metaPosition.append(i)
                    self.metaPosition.append(j)
        return(self.metaPosition)

    def getCostPosition(self):
        self.costPosition=[]
        for i in range(self.matrixSize):
            for j in range(self.matrixSize):
                if (self.matrix[i][j]=="C"):
                    self.costPosition.append([i,j])
        return(self.costPosition)

    def processingDataList(self,dataList):
        self.matrix=[]
        self.matrixSize=(int)(dataList.pop(0).replace(",",""))
        for i in range(len(dataList)):
            auxList=[]
            for j in range(len(dataList[i])):
                if(dataList[i][j]!=","):
                    auxList.append((str)(dataList[i][j]))
            self.matrix.append(auxList)
#==============================================================================