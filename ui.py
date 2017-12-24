from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setupMainWindow(MainWindow)

        self.setupCentralWidget(MainWindow)

        self.setupMainWidget(MainWindow)

        self.setupSniffingWidget(MainWindow)
        self.sniffingWidget.hide()

        self.setupToolbar(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupMainWindow(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(760, 604)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(760, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/windowIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

    def setupCentralWidget(self, MainWindow):
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))


    def setupMainWidget(self, MainWindow):
        self.mainWidget = QtGui.QWidget(self.centralwidget)
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.mainWidget)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_9 = QtGui.QLabel(self.mainWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bauhaus 93"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtGui.QFrame.Plain)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.mainWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MV Boli"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        spacerItem1 = QtGui.QSpacerItem(1000, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        spacerItem2 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem3 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)

        self.listView = QtGui.QListWidget(self.mainWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.horizontalLayout_12.addWidget(self.listView)

        spacerItem4 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        spacerItem5 = QtGui.QSpacerItem(5, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem6 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)

        self.sniffButton = QtGui.QCommandLinkButton(self.mainWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sniffButton.sizePolicy().hasHeightForWidth())
        self.sniffButton.setSizePolicy(sizePolicy)
        self.sniffButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sniffButton.setCheckable(False)
        self.sniffButton.setAutoDefault(True)
        self.sniffButton.setObjectName(_fromUtf8("sniffButton"))
        self.horizontalLayout_13.addWidget(self.sniffButton)

        spacerItem7 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.verticalLayout_10.addLayout(self.verticalLayout_4)

        self.verticalLayout_9.addWidget(self.mainWidget)
        MainWindow.setCentralWidget(self.centralwidget)

    def setupSniffingWidget(self, MainWindow):
        self.sniffingWidget = QtGui.QWidget(self.centralwidget)
        self.sniffingWidget.setObjectName(_fromUtf8("sniffingWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.sniffingWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.sniffingWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))

        self.tableWidget = QtGui.QTableWidget(self.splitter)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSortingEnabled(True)

        self.tableWidget.horizontalHeader().setResizeMode(6, QtGui.QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(6, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.treeWidget = QtGui.QTreeWidget(self.splitter)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setObjectName(_fromUtf8("treeView"))
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderHidden(True)

        self.textEdit = QtGui.QTextEdit(self.splitter)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.splitter)

        self.verticalLayout_9.addWidget(self.sniffingWidget)
        MainWindow.setCentralWidget(self.centralwidget)

    def setupToolbar(self, MainWindow):
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon1)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))

        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setCheckable(False)
        self.actionStop.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon2)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))

        self.actionRestart = QtGui.QAction(MainWindow)
        self.actionRestart.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Restart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestart.setIcon(icon3)
        self.actionRestart.setObjectName(_fromUtf8("actionRestart"))

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/Home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon5)
        self.actionHome.setVisible(True)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))

        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionRestart)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionSave)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Packet Sniffer", None))
        self.label_9.setText(_translate("MainWindow", "Welcome to Packet Sniffer", None))
        self.label_10.setText(_translate("MainWindow", "By: Enigma Team", None))
        self.sniffButton.setText(_translate("MainWindow", "Capture", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionRestart.setText(_translate("MainWindow", "Restart", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
