#==============================================================================
#===============================Import Libraries===============================
#==============================================================================
import sys
sys.path.append("..")
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#==============================================================================


#==============================================================================
#=================================Main Window==================================
#==============================================================================
class MainWindow(QMainWindow):

    def __init__(self,appModel,appController):
        super(MainWindow,self).__init__()
        self.appModel=appModel
        self.appController=appController
        self.initWindow()
        self.initWidgets()
        self.initToolbar()
        self.initMenu()
        self.initStatusBar()
        self.initSignals()

    #==========================================================================
    #==================================Window==================================
    #==========================================================================
    def initWindow(self):
        self.setWindowTitle(self.tr("Artificial Intelligence"))
        self.setWindowIcon(QIcon("Image/Logo.ico"))
        self.setMinimumSize(550,650)
        self.centerWindow()

    def centerWindow(self):
        window=self.frameGeometry()
        centerPoint=QDesktopWidget().availableGeometry().center()
        window.moveCenter(centerPoint)
        self.move(window.topLeft())

    #==========================================================================
    #==================================Widgets=================================
    #==========================================================================
    def initWidgets(self):
        self.botonExit=QAction("Exit",self)
        self.botonExit.setIcon(QIcon("Image/Exit.ico"))
        self.botonExit.setShortcut("Ctrl+Q")
        self.botonExit.setStatusTip(self.trUtf8("Exit the application."))

        self.botonOpenFile=QAction("Open File",self)
        self.botonOpenFile.setIcon(QIcon("Image/OpenFile.ico"))
        self.botonOpenFile.setShortcut("Ctrl+E")
        self.botonOpenFile.setStatusTip(self.trUtf8("Open the file with the input data."))

        self.botonHelp=QAction("Help",self)
        self.botonHelp.setIcon(QIcon("Image/Help.ico"))
        self.botonHelp.setShortcut("Ctrl+N")
        self.botonHelp.setStatusTip(self.trUtf8("Application help."))

        self.botonAbout=QAction("About",self)
        self.botonAbout.setShortcut("Ctrl+M")
        self.botonAbout.setStatusTip(self.trUtf8("About the application."))

    def newWidgetsOne(self):
        self.initLabel()
        self.initLineEdit()
        self.initComboBox()
        self.initButton()
        self.initSlider()
        self.initGroupBox()
        self.initGridLayout()
        self.signals()
        self.controlGroupOne.setLayout(self.controlLayout)
        self.mainWidget=QWidget(self)
        mainLayout=QVBoxLayout(self.mainWidget)
        mainLayout.addWidget(self.controlGroupOne)
        self.controlGroupTwo.setLayout(self.controlLayoutTwo)
        mainLayout.addWidget(self.controlGroupTwo)
        self.controlGroupThree.setLayout(self.controlLayoutThree)
        mainLayout.addWidget(self.controlGroupThree)
        self.mainWidget.setFocus()
        self.setCentralWidget(self.mainWidget)

    #==========================================================================
    #==================================Toolbar=================================
    #==========================================================================
    def initToolbar(self):
        self.toolbar=QToolBar(self)
        self.toolbar.addAction(self.botonExit)
        self.toolbar.addAction(self.botonOpenFile)
        self.toolbar.addAction(self.botonHelp)
        self.addToolBar(self.toolbar)

    #==========================================================================
    #===================================Menu===================================
    #==========================================================================
    def initMenu(self):
        menu=self.menuBar()

        fileMenu=menu.addMenu("File")
        fileMenu.addAction(self.botonOpenFile)
        fileMenu.addAction(self.botonExit)

        helpMenu=menu.addMenu("Help")
        helpMenu.addAction(self.botonHelp)
        helpMenu.addAction(self.botonAbout)

    #==========================================================================
    #===================================Label==================================
    #==========================================================================
    def initLabel(self):
        self.labelOne=QLabel("Uninformed Search:")
        self.labelTwo=QLabel("Informed Search:")
        self.labelThree=QLabel("Graphic Simulation:")
        self.labelFour=QLabel("Created Nodes:")
        self.labelFive=QLabel("Tree Depth:")
        self.labelSix=QLabel("Search Cost:")
        self.labelSeven=QLabel("Runtime:")

    #==========================================================================
    #=================================LineEdit=================================
    #==========================================================================
    def initLineEdit(self):
        self.lineEditOne=QLineEdit()
        #self.lineEditOne.setEnabled(False)
        self.lineEditOne.setToolTip("Created Nodes")
        self.lineEditOne.setStatusTip(self.trUtf8("Number of nodes created in the tree."))

        self.lineEditTwo=QLineEdit()
        #self.lineEditTwo.setEnabled(False)
        self.lineEditTwo.setToolTip("Tree Depth")
        self.lineEditTwo.setStatusTip(self.trUtf8("Depth of the search tree."))

        self.lineEditThree=QLineEdit()
        #self.lineEditThree.setEnabled(False)
        self.lineEditThree.setToolTip("Search Cost")
        self.lineEditThree.setStatusTip(self.trUtf8("Cost search algorithm."))

        self.lineEditFour=QLineEdit()
        #self.lineEditFour.setEnabled(False)
        self.lineEditFour.setToolTip("Runtime")
        self.lineEditFour.setStatusTip(self.trUtf8("Runtime search algorithm."))

    #==========================================================================
    #==================================Button==================================
    #==========================================================================
    def initButton(self):
        self.botonOne=QPushButton("Start Search",self)
        self.botonOne.setToolTip("Start Search")
        self.botonOne.setStatusTip(self.trUtf8("Start path search algorithm."))

    #==========================================================================
    #=================================ComboBox=================================
    #==========================================================================
    def initComboBox(self):
        self.comboOne=QComboBox()
        self.comboOne.setToolTip("Uninformed Search")
        self.comboOne.setStatusTip(self.trUtf8("Uninformed search algorithms."))
        dataList=["","Breadth First Search","Uniform Cost Search","Depth First Search"]
        for item in dataList:
            self.comboOne.addItem(item)

        self.comboTwo=QComboBox()
        self.comboTwo.setToolTip("Informed Search")
        self.comboTwo.setStatusTip(self.trUtf8("Informed search algorithms."))
        dataList=["","Avara Search","Star Search"]
        for item in dataList:
            self.comboTwo.addItem(item)

    #==========================================================================
    #==================================Slider==================================
    #==========================================================================
    def initSlider(self):
        self.slider=QSlider(Qt.Vertical)
        self.slider.setToolTip("Slider")
        self.slider.setRange(0,6*3)
        self.slider.setTickPosition(QSlider.TicksRight)
        self.slider.setValue(3*3)

    #==========================================================================
    #=================================GroupBox=================================
    #==========================================================================
    def initGroupBox(self):
        self.controlGroupOne=QGroupBox("Graphic Simulation")
        self.controlGroupTwo=QGroupBox("Search Algorithms")
        self.controlGroupThree=QGroupBox("Output Data")

    #==========================================================================
    #================================GridLayout================================
    #==========================================================================
    def initGridLayout(self):
        self.dataTable=self.appController.createDataTable()
        self.controlLayout=QGridLayout()
        self.controlLayoutTwo=QGridLayout()
        self.controlLayoutThree=QGridLayout()

        self.controlLayout.addWidget(self.dataTable,0,0)
        self.controlLayout.addWidget(self.slider,0,1)
        self.controlLayoutTwo.addWidget(self.labelOne,0,0)
        self.controlLayoutTwo.addWidget(self.comboOne,0,1)
        self.controlLayoutTwo.addWidget(self.labelTwo,0,2)
        self.controlLayoutTwo.addWidget(self.comboTwo,0,3)
        self.controlLayoutThree.addWidget(self.labelFour,0,0)
        self.controlLayoutThree.addWidget(self.labelFive,1,0)
        self.controlLayoutThree.addWidget(self.labelThree,2,0)
        self.controlLayoutThree.addWidget(self.lineEditOne,0,1)
        self.controlLayoutThree.addWidget(self.lineEditTwo,1,1)
        self.controlLayoutThree.addWidget(self.botonOne,2,1)
        self.controlLayoutThree.addWidget(self.labelSix,0,2)
        self.controlLayoutThree.addWidget(self.labelSeven,1,2)
        self.controlLayoutThree.addWidget(self.lineEditThree,0,3)
        self.controlLayoutThree.addWidget(self.lineEditFour,1,3)

    #==========================================================================
    #================================Status Bar================================
    #==========================================================================
    def initStatusBar(self):
        self.setStatusBar(QStatusBar())

    #==========================================================================
    #==================================Signals=================================
    #==========================================================================
    def initSignals(self):
        self.connect(self.botonExit,SIGNAL("triggered()"),self.appController.functionExit)
        self.connect(self.botonOpenFile,SIGNAL("triggered()"),self.appController.functionOpenFile)
        self.connect(self.botonHelp,SIGNAL("triggered()"),self.appController.functionHelp)
        self.connect(self.botonAbout,SIGNAL("triggered()"),self.appController.functionAbout)

    def signals(self):
        self.connect(self.botonOne,SIGNAL("clicked()"),self.appController.startSearch)
        self.connect(self.slider,SIGNAL("valueChanged(int)"),self.dataTable.setSliderValue)
        self.connect(self.comboOne,SIGNAL("activated(QString)"),self.appController.searchAlgorithm)
        self.connect(self.comboTwo,SIGNAL("activated(QString)"),self.appController.searchAlgorithm)
#==============================================================================