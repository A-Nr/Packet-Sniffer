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
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtGui.QFrame.Plain)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.mainWidget)
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Packet Sniffer", None))
        self.label_9.setText(_translate("MainWindow", "Welcome to Packet Sniffer", None))
        self.label_10.setText(_translate("MainWindow", "By: Enigma Team", None))
        self.sniffButton.setText(_translate("MainWindow", "Capture", None))
