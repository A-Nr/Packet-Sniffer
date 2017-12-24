from PyQt4 import QtCore
from scapy.all import *


class SniffPacketsThread(QtCore.QThread):

    def __init__(self, device, fltr = None):
        QtCore.QThread.__init__(self)
        self.device = device
        self.fltr = fltr
        self.paktsList = []
        self.end = False

    def __del__(self):
        self.wait()

    def endSniffing(self):
        self.end = True

    def sniffIsFinished(self):
        return self.end

    def handlePacket(self,packet):
        self.paktsList.append(packet)
        tableViewPart = dict()
        tableViewPart['timestamp'] = packet.time
        try:
            tableViewPart['source'] = packet.getlayer("IP").src
            tableViewPart['destination'] = packet.getlayer("IP").dst
        except:
            tableViewPart['source'] = packet.src
            tableViewPart['destination'] = packet.dst
        tableViewPart['length'] = len(packet)
        tableViewPart['layers'] = self.getLayers(packet)

        (protocol,info) = self.getInfo(packet)
        tableViewPart['info'] = info

        if protocol:
            tableViewPart['Protocol'] = protocol
        elif IP in packet:
            tableViewPart['Protocol'] = "IP"
        else:
            tableViewPart['Protocol'] = "Other"

        self.emit(QtCore.SIGNAL('addPacketToTableWidget(PyQt_PyObject)'), (packet, tableViewPart))

    def getLayers(self,packet):
        layers = []
        counter = 0
        while True:
            layer = packet.getlayer(counter)
            if layer != None:
                if layer.name != "Padding":
                    layers.append(layer.name)
            else:
                break
            counter += 1
        return layers

    def getInfo(self,packet):
        info = ""
        protocol = ""
        if UDP in packet:
            protocol = "UDP"
            info = "{} -> {} len={} chksum={}".format(packet[UDP].sport,
                                                      packet[UDP].dport,
                                                      packet[UDP].len,
                                                      packet[UDP].chksum)
        elif TCP in packet:
            flags = {
                'F': 'FIN',
                'S': 'SYN',
                'R': 'RST',
                'P': 'PSH',
                'A': 'ACK',
                'U': 'URG',
                'E': 'ECE',
                'C': 'CWR',
            }
            flgs = str([flags[x] for x in packet.sprintf('%TCP.flags%')])
            protocol = "TCP"
            info = "{} -> {} {} seq={} ack={} window={}".format(packet[TCP].sport,
                                                                packet[TCP].dport,
                                                                flgs,
                                                                packet[TCP].seq,
                                                                packet[TCP].ack,
                                                                packet[TCP].window)
        elif ARP in packet:
            protocol = "ARP"
            info = "hwtype={} ptype={} hwlen={} plen={} op={}".format(packet[ARP].hwtype,
                                                                      packet[ARP].ptype,
                                                                      packet[ARP].hwlen,
                                                                      packet[ARP].plen,
                                                                      packet[ARP].op)
        return (protocol,info)

    def run(self):
        self.pkts = sniff(count=0, filter=self.fltr, iface=self.device,
                          prn=self.handlePacket, stop_callback=self.sniffIsFinished)