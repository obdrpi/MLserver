import re

def sqlInjection(http_payload):
	try:
		regex = re.compile(r"((WHERE|OR|AND|or|and)[ ]+[\(]*[ ]*([\(]*[0-9]+[\)]*)[ ]*=[ ]*[\)]*[ ]*\3)|AND[ ]+[\(]*[ ]*([\(]*1[0-9]+|[2-9][0-9]*[\)]*)[ ]*[\(]*[ ]*=[ ]*[\)]*[ ]*\4")
		match = regex.search(http_payload)
		if match:
			return 1
		else:
			return 0
	except:
		print "Unknown Exception"

	return None

def puncChars(http_payload):
	try:
		regex = re.compile(r"['.?;\":,!()-]+")
		i = 0
		count = 0
		while True:
			match = regex.search(http_payload, i)
			if match:
				#print match.start()
				i = match.start() + 1
				count = count + 1
			else:
				break

	except:
		print "Unknow Exception"

	return count

def commInjection(http_payload):
	try:
		regex = re.compile(r";(ls|rm|cat)+")
		match = regex.search(http_payload)
		if match:
			return 1
		else:
			return 0	
	except:
		print "Unknown Exception"

def length(http_payload):
	lent = 0
	try:
		lent = len(http_payload)
		
	except:	
		print "Unknown Exception"
	return lent

def entropy(http_payload):
	try:
		print "f"
	except:	
		print "h"

