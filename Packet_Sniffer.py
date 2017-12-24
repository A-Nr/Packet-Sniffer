from PyQt4 import QtGui,QtCore
from scapy.all import *
from io import StringIO
from SniffThread import SniffPacketsThread
import ui
import time
import sys
import os

class App(QtGui.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        self.initList()

        self.actionStart.triggered.connect(self.startSniffing)
        self.actionStop.triggered.connect(self.stopSniffing)
        self.actionRestart.triggered.connect(self.restartSniffing)
        self.actionHome.triggered.connect(self.loadHomePage)
        self.actionSave.triggered.connect(self.savePackets)
        self.sniffButton.clicked.connect(self.startSniffing)
        self.tableWidget.clicked.connect(self.showPacketData)

    def initList(self):
        self.listView.clear()
        for iface_name in sorted(ifaces.keys()):
            dev = ifaces[iface_name]
            mac = dev.mac
            if iface_name != LOOPBACK_NAME:
                mac = conf.manufdb._resolve_MAC(mac)
            item = "%s\t%s\t\t%s\t\t%s" % (str(dev.win_index).ljust(5), str(dev.name).ljust(35), str(dev.ip).ljust(15), mac)
            self.listView.addItem(item)

    def getSniffingDevice(self):
        a = self.listView.selectedIndexes()
        idx = a[0].data()
        idx = idx.split('\t')
        idx = idx[1]
        idx = idx.strip()
        # device = ifaces[idx]
        return idx

    def switchScreen(self):
        if not self.mainWidget.isHidden():
            self.mainWidget.hide()
        if self.sniffingWidget.isHidden():
            self.sniffingWidget.show()
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)


    def switchScreenBack(self):
        if not self.sniffingWidget.isHidden():
            self.sniffingWidget.hide()
        if self.mainWidget.isHidden():
            self.mainWidget.show()
        self.initList()

    def addPacketToTableWidget(self,data):
        tableData = data[1]
        rowpos = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowpos)
        self.tableWidget.setItem(rowpos, 0, QtGui.QTableWidgetItem(str(rowpos+1)))
        self.tableWidget.setItem(rowpos, 1, QtGui.QTableWidgetItem(str(tableData['timestamp'])))
        self.tableWidget.setItem(rowpos, 2, QtGui.QTableWidgetItem(tableData['source']))
        self.tableWidget.setItem(rowpos, 3, QtGui.QTableWidgetItem(tableData['destination']))
        self.tableWidget.setItem(rowpos, 4, QtGui.QTableWidgetItem(tableData['Protocol']))
        self.tableWidget.setItem(rowpos, 5, QtGui.QTableWidgetItem(str(tableData['length'])))
        self.tableWidget.setItem(rowpos, 6, QtGui.QTableWidgetItem(tableData['info']))
        # self.tableWidget.scrollToBottom()

    def showPacketData(self):
        a = self.tableWidget.selectedItems()
        idx = int(a[0].text()) - 1
        self.showHexDump(idx)
        self.showTreeData(idx)

    def showHexDump(self, packetIndex):
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        hexdump(self.sniffingThread.paktsList[packetIndex])
        sys.stdout = save_stdout
        self.textEdit.setText(capture.getvalue())

    def showTreeData(self, packetIndex):
        self.treeWidget.clear()
        capture = StringIO()
        save_stdout = sys.stdout
        sys.stdout = capture
        packet = self.sniffingThread.paktsList[packetIndex]
        packet.show2()
        sys.stdout = save_stdout
        data = capture.getvalue()

        first = QtGui.QTreeWidgetItem(self.treeWidget, ["frame {}: size {}".format(packetIndex+1, len(packet))])
        firsta = QtGui.QTreeWidgetItem(first,["Encapsulation type: {}".format(packet[0].name)])
        firstb = QtGui.QTreeWidgetItem(first,["Arrival time: {}".format(time.strftime('%a, %d %b %Y %H:%M:%S GMT',
                                                                                    time.localtime(packet[0].time)))])
        firstc = QtGui.QTreeWidgetItem(first,["Frame Number: {}".format(packetIndex+1)])
        firstc = QtGui.QTreeWidgetItem(first,["Frame length: {}".format(len(packet))])

        a = None
        for line in data.splitlines():
            if line.startswith("###["):
                line = line.rstrip(" ###]")
                line = line.lstrip("[### ")
                a = QtGui.QTreeWidgetItem(self.treeWidget, [line])
            else:
                line = line.strip()
                QtGui.QTreeWidgetItem(a, [line])

    def startSniffing(self):
        if not self.mainWidget.isHidden():
            while True:
                try:
                    self.device = self.getSniffingDevice()
                    break
                except IndexError:
                    QtGui.QMessageBox.information(self, "Error", "You didn't choose an interface")
                    return

        self.actionStart.setEnabled(False)
        self.actionStop.setEnabled(True)
        self.actionSave.setEnabled(False)
        self.actionRestart.setEnabled(True)
        self.actionHome.setEnabled(True)

        self.sniffingThread = SniffPacketsThread(self.device)
        self.connect(self.sniffingThread, QtCore.SIGNAL('addPacketToTableWidget(PyQt_PyObject)'),
                     self.addPacketToTableWidget)

        self.actionStop.triggered.connect(self.sniffingThread.endSniffing)
        self.actionHome.triggered.connect(self.sniffingThread.endSniffing)

        self.switchScreen()
        self.sniffingThread.start()

    def stopSniffing(self):
        self.actionStart.setEnabled(True)
        self.actionStop.setEnabled(False)
        self.actionHome.setEnabled(True)
        self.actionSave.setEnabled(True)
        self.actionRestart.setEnabled(False)

    def restartSniffing(self):
        self.actionStart.setEnabled(False)
        self.actionStop.setEnabled(True)
        self.actionSave.setEnabled(False)
        self.actionRestart.setEnabled(True)
        self.actionHome.setEnabled(True)

        self.sniffingThread.terminate()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.sniffingThread.start()

    def loadHomePage(self):
        self.actionStart.setEnabled(True)
        self.actionStop.setEnabled(False)
        self.actionSave.setEnabled(False)
        self.actionRestart.setEnabled(False)
        self.actionHome.setEnabled(False)

        self.switchScreenBack()

    def savePackets(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".pcap")
        if filename.find(".pcap") == -1:
            filename += ".pcap"
        wrpcap(filename, self.sniffingThread.pkts)