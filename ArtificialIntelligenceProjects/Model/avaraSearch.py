#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
import math
from queue import PriorityQueue
#==============================================================================


#==============================================================================
#=================================Avara Search=================================
#==============================================================================
class AvaraSearch(object):

    def __init__(self,startPosition,metaPosition,costPosition,maze):
        self.startPosition=startPosition
        self.metaPosition=metaPosition
        self.costPosition=costPosition
        self.maze=maze
        self.createdNodes=0
        self.searchCost=0
        self.treeDepth=0
        self.costValue=5
        self.nodeList=self.searchPath()

    def getCreatedNodes(self):
        return(self.createdNodes)

    def getSearchCost(self):
        return(self.searchCost)

    def getTreeDepth(self):
        return(self.treeDepth)

    def getPath(self):
        path=[]
        while(self.nodeList!=None):
            path.append((self.nodeList[1],self.nodeList[2]))
            self.nodeList=self.nodeList[3]
        path.reverse()
        self.searchCost=self.getCost(path)-1
        self.treeDepth=len(path)-1
        return(path)

    def getCost(self,path):
        cost=0
        counter=0
        for i in range(len(path)):
            for j in range(len(self.costPosition)):
                if([path[i][0],path[i][1]]==[self.costPosition[j][0],self.costPosition[j][1]]):
                    cost+=self.costValue
                    counter+=1
        cost+=len(path)-counter
        return(cost)

    def calculateHeuristic(self,x,y):
        dx=abs(x-self.metaPosition[0])
        dy=abs(y-self.metaPosition[1])
        return(math.sqrt((dx*dx)+(dy*dy)))

    def searchPath(self):
        queue=PriorityQueue() #create priority queue
        queue.put([0,self.startPosition[0],self.startPosition[1],None]) #add the start point to the tail
        while(queue.qsize()>0): #make sure there are nodes to check left
            nodeList=queue.get() #grab the first node
            x=nodeList[1] #get x
            y=nodeList[2] #get y
            if(self.maze[x][y]=="M"): #check if it's an meta
                self.reconstructMaze() #reconstruct the maze
                return(nodeList) #if it is then return the path
            if(self.maze[x][y]!="0"): #if it's not a path, we can't try this spot
                if((self.maze[x][y]=="S")or(self.maze[x][y]=="C")): #discard the starting point and the cost
                    pass #continue executing the algorithm
                else: #does not meet the condition
                    continue #return to the beginning of the loop
            self.maze[x][y]="explored" #make this spot explored so we don't try again
            for i in ([x,y-1],[x,y+1],[x-1,y],[x+1,y]): #new spots to try
                self.createdNodes+=1 #count the number of nodes created
                queue.put((self.calculateHeuristic(i[0],i[1]),i[0],i[1],nodeList)) #create the new spot, with node as the parent
        return([]) #return the empty list since we couldn't find any paths from here

    def reconstructMaze(self):
        self.maze[self.startPosition[0]][self.startPosition[1]]="S"
        for row in range(len(self.maze)):
            for column in range(len(self.maze)):
                if (self.maze[row][column]=="explored"):
                    self.maze[row][column]="0"
        for index in range(len(self.costPosition)):
            self.maze[self.costPosition[index][0]][self.costPosition[index][1]]="C"
#==============================================================================