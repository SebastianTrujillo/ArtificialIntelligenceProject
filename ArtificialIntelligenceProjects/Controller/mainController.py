#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
import sys
sys.path.append("..")
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from View import mainWindow
from View import canvas
from time import time
from Model import breadthFirstSearch
from Model import uniformCostSearch
from Model import depthFirstSearch
from Model import avaraSearch
from Model import starSearch
#==============================================================================


#==============================================================================
#===============================Main Controller================================
#==============================================================================
class MainController(object):

    def __init__(self,appModel):
        self.path=None
        self.applySearch=False
        self.appModel=appModel
        self.window=mainWindow.MainWindow(self.appModel,self)
        self.window.show()

    def functionExit(self):
        self.window.close()

    def functionOpenFile(self):
        inputError=False
        directory="DataInput"
        try:
            fileName=QFileDialog.getOpenFileName(self.window,"Abrir archivo",directory)
            with open(fileName,"r") as fileContent:
                dataList=[line.rstrip("\n") for line in fileContent]
            self.appModel.processingDataList(dataList)
        except IOError:
            inputError=True
        except:
            inputError=True
            self.firstInformationMessage()
        if(not(inputError)):
            self.window.newWidgetsOne()

    def functionHelp(self):
        QMessageBox.question(self.window, "Help - Artificial Intelligence",
        """
        ========================================================

        Description of problem:

        The Universidad del Valle has built a prototype robot named Ubicame UV,
        whose task is to locate people when they want to find some teacher or
        University website, the Robot has information environment consisting of
        obstacles to its initial location and aims. The environment is represented
        by an integer array of size n×n.

        ========================================================
        """)

    def functionAbout(self):
        QMessageBox.information(self.window, "About - Artificial Intelligence",
        """
        ========================================================

        Artificial intelligence has been developed by Juan Sebastian Rodriguez
        with the Python programming language in Version 3.4 implements the
        QT4 library Version 4.11 to generate its GUI and PyOpenGL in Version
        3.1 to generate the graphic design. For more information write to email
        rodrigueztrujillojuan@hotmail.com

        ========================================================
        """)

    def firstInformationMessage(self):
        print("File is empty... \n")
        QMessageBox.information(self.window, "Information - Artificial Intelligence",
        """
        =================================

        File is empty.

        =================================
        """)

    def secondInformationMessage(self):
        print("Not Connected...\n")
        QMessageBox.information(self.window, "Information - Artificial Intelligence",
        """
        =================================

        Search not connected to the GUI.

        =================================
        """)

    def thirdInformationMessage(self):
        print("Select a search type...\n")
        QMessageBox.information(self.window, "Information - Artificial Intelligence",
        """
        =================================

        Select a search type.

        =================================
        """)

    def searchAlgorithm(self,value):
        if(value=="Breadth First Search"):
            self.applySearch=True
            print("\nBreadth First Search: \n")
            firstUninformedSearch=breadthFirstSearch.BreadthFirstSearch(self.appModel.getStartPosition(),self.appModel.getCostPosition(),self.appModel.getMatrix())
            startTime=time()
            self.path=firstUninformedSearch.getPath()
            elapsedTime=time()-startTime
            print("Path: ",self.path,"\n")
            self.window.lineEditOne.setText((str)(firstUninformedSearch.getCreatedNodes()))
            self.window.lineEditTwo.setText((str)(firstUninformedSearch.getTreeDepth()))
            self.window.lineEditThree.setText((str)(firstUninformedSearch.getSearchCost()))
            self.window.lineEditFour.setText("%.4f Seconds" % elapsedTime)
            self.disableComboTwo()

        elif(value=="Uniform Cost Search"):
            self.applySearch=True
            print("\nUniform Cost Search: \n")
            secondUninformedSearch=uniformCostSearch.UniformCostSearch(self.appModel.getStartPosition(),self.appModel.getCostPosition(),self.appModel.getMatrix())
            startTime=time()
            self.path=secondUninformedSearch.getPath()
            elapsedTime=time()-startTime
            print("Path: ",self.path,"\n")
            self.window.lineEditOne.setText((str)(secondUninformedSearch.getCreatedNodes()))
            self.window.lineEditTwo.setText((str)(secondUninformedSearch.getTreeDepth()))
            self.window.lineEditThree.setText((str)(secondUninformedSearch.getSearchCost()))
            self.window.lineEditFour.setText("%.4f Seconds" % elapsedTime)
            self.disableComboTwo()

        elif(value=="Depth First Search"):
            self.applySearch=True
            print("\nDepth First Search: \n")
            thirdUninformedSearch=depthFirstSearch.DepthFirstSearch(self.appModel.getStartPosition(),self.appModel.getCostPosition(),self.appModel.getMatrix())
            startTime=time()
            self.path=thirdUninformedSearch.getPath()
            elapsedTime=time()-startTime
            print("Path: ",self.path,"\n")
            self.window.lineEditOne.setText((str)(thirdUninformedSearch.getCreatedNodes()))
            self.window.lineEditTwo.setText((str)(thirdUninformedSearch.getTreeDepth()))
            self.window.lineEditThree.setText((str)(thirdUninformedSearch.getSearchCost()))
            self.window.lineEditFour.setText("%.4f Seconds" % elapsedTime)
            self.disableComboTwo()

        elif(value=="Avara Search"):
            self.applySearch=True
            print("\nAvara Search: \n")
            firstInformedSearch=avaraSearch.AvaraSearch(self.appModel.getStartPosition(),self.appModel.getMetaPosition(),self.appModel.getCostPosition(),self.appModel.getMatrix())
            startTime=time()
            self.path=firstInformedSearch.getPath()
            elapsedTime=time()-startTime
            print("Path: ",self.path,"\n")
            self.window.lineEditOne.setText((str)(firstInformedSearch.getCreatedNodes()))
            self.window.lineEditTwo.setText((str)(firstInformedSearch.getTreeDepth()))
            self.window.lineEditThree.setText((str)(firstInformedSearch.getSearchCost()))
            self.window.lineEditFour.setText("%.4f Seconds" % elapsedTime)
            self.disableComboOne()

        elif(value=="Star Search"):
            self.applySearch=True
            print("\nStar Search: \n")
            secondInformedSearch=starSearch.StarSearch(self.appModel.getStartPosition(),self.appModel.getMetaPosition(),self.appModel.getCostPosition(),self.appModel.getMatrix())
            startTime=time()
            self.path=secondInformedSearch.getPath()
            elapsedTime=time()-startTime
            print("Path: ",self.path,"\n")
            self.window.lineEditOne.setText((str)(secondInformedSearch.getCreatedNodes()))
            self.window.lineEditTwo.setText((str)(secondInformedSearch.getTreeDepth()))
            self.window.lineEditThree.setText((str)(secondInformedSearch.getSearchCost()))
            self.window.lineEditFour.setText("%.4f Seconds" % elapsedTime)
            self.disableComboOne()

    def startSearch(self):
        if(self.applySearch):
            self.window.dataTable.startSimulation(self.path)
            self.applySearch=False
            self.clearCombo()
        else:
            self.thirdInformationMessage()

    def createDataTable(self):
        return(canvas.GLWidget(self,self.appModel.getMatrixSize(),self.appModel.getMatrix()))

    def disableComboOne(self):
        self.window.comboOne.setEnabled(False)
        self.window.comboTwo.setEnabled(True)

    def disableComboTwo(self):
        self.window.comboOne.setEnabled(True)
        self.window.comboTwo.setEnabled(False)

    def clearCombo(self):
        self.window.comboOne.setEnabled(True)
        self.window.comboOne.setCurrentIndex(0)
        self.window.comboTwo.setEnabled(True)
        self.window.comboTwo.setCurrentIndex(0)
#==============================================================================