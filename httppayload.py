from scapy.all import *
import urllib
import csv
from analyzeHTTPPayload import sqlInjection, puncChars, length, commInjection


def exportcsv(sip, sport, dip, dport, ipver, prot, sqlinj, comminj, punc, leng):

	try:
		with open('file.csv', 'a') as f:
    			w = csv.writer(f, delimiter = ',', quoting=csv.QUOTE_NONE)
			if sqlinj == 1:
				malicious = 1
			else:
				malicious = 0
			w.writerow([sport, dport, ipver, prot, sqlinj, comminj, punc, leng, malicious])
			#w.writerow(['r', 'k', 'y'])
	except:
		print "Error"			

def process(http_payload):
                          	print "Printing HTTPayload"
                                http_payload1 = " ".join(http_payload.split())
                                http_payload2 = urllib.unquote_plus(http_payload1)
                                print http_payload2
                                #print "Whether it is a SQL Injection or not:"
                                global sqlinj
				sqlinj = sqlInjection(http_payload2)
                                #print "No of punctuation chracters:"
                                global punc
				punc = puncChars(http_payload2)
                                #print "Length of the HTTP payload:"
                                global leng
				leng = length(http_payload2)
				global comminj
				comminj = commInjection(http_payload2)

os.system("tshark -r /root/Eavesdrop_Data.pcap -Y http -w /root/Eavesdrop_Data_http.pcap")
data = "/root/Eavesdrop_Data_http.pcap"
a = rdpcap(data)
#os.system("tshark -i lo -T fields -e http -e frame.time -e data.data -w Eavesdrop_Data.pcap > Eavesdrop_Data.txt -c 10")
#os.system("tshark -r /root/Eavesdrop_Data.pcap -Y http -w /root/Eavesdrop_Data_http.pcap")
sessions = a.sessions()
i = 1
for session in sessions:
    http_payload = ""
    for packet in sessions[session]:
        try:
		global sqlinj
		global punc
		global leng
		global comminj
		#print "Session summary" + str(packet.summary())
		#print "Session" + str(packet.show())
		prot = packet[IP].proto
		sip = str(packet[IP].src)
		dip =  str(packet[IP].dst)
		sport = str(packet[IP].sport)
		dport = str(packet[IP].dport)
		ipver = packet[IP].version
		print ipver
		if prot == 6:
			if packet[TCP].dport == 8000: # or packet[UDP].dport == 8000: #or packet[TCP].sport == 8000:
                		http_payload = str(packet[TCP].payload)
				process(http_payload)	#print packet[TCP].payload
				
		elif prot == 17:
			if packet[UDP].dport == 8000:
				http_payload = str(packet[UDP].payload)
                                process(http_payload)
		elif prot == 1:
			if packet[ICMP].dport == 8000:
				http_payload = str(packet[ICMP].payload)
                                process(http_payload)	
		else:
			print "Unknown protocol"
		print sip, sport, dip, dport, ipver, prot, sqlinj, punc, leng
		exportcsv(sip, sport, dip, dport, ipver, prot, sqlinj, comminj, punc, leng)

	except:
            pass
