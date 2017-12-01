import os
from scapy.all import *
os.system("tshark -i lo -T fields -e frame.time -e data -w /root/Eavesdrop_Data.pcap > Eavesdrop_Data.txt -F pcap -c 3000")
#data = "Eavesdrop_Data.pcap"
#a = rdpcap(data)
