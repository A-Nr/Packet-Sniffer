
##Introduction 
+ Wireshark is the best packet analyzer program. Many network engineers used it in order to solve communication issues. 
+ You can find many jobs require Wireshark for a network engineer with average salary $88000 in US. 
+ Now, after being familiar with Wireshark and its feature, our target is to build our own packet analyzer that is similar to Wireshark.
##Our Project:
Packet Sniffer Program using Python, Scapy and Pyqt4
##Dependencies
+ Python3
+ [scapy](https://github.com/phaethon/scapy)
+ [PyQt4](https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py3.4-Qt5.5.0-x64.exe/download)
##Features
+ Multi-Threading
+ Packet Sniffing showing various information about the packet, such as: 
++ Packet Protocol
++ Payload
++ Source and Destination addresses
++ Time
++ Packet Length
++ Packet Information
++ Data Hex Presentation
+ Ability to select available interface
+ Ability to save a (.pcap) file
+ User-Friendly GUI
## Usage
1. Start the program with `python3 main.py`
2. Choose the required interface for sniffing
3. Click `Capture` or the `green Start button`

