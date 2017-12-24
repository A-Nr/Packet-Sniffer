from Packet_Sniffer import *

def main():
    app = QtGui.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()