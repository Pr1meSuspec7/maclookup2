#!/usr/bin/python3

import requests
import sys
import time

def checkarg():
	if len(sys.argv) < 2:
		print('The argument must be a mac address write in any form:\n00-11-22-33-44-55\n00:11:22:33:44:55\n00.11.22.33.44.55\n001122334455\n0011.2233.4455\n\n\
	Ex. maclookup2.py 3C6AA771CCCB 00:50:56:C0:00:02 E4-B9-7A-08-C9-EF 001C.7F00.00010\n')
		sys.exit()
	elif sys.argv[1] == 'help':
		print('The argument must be a mac address write in any form:\n00-11-22-33-44-55\n00:11:22:33:44:55\n00.11.22.33.44.55\n001122334455\n0011.2233.4455\n\n\
	Ex. maclookup2.py 3C6AA771CCCB 00:50:56:C0:00:02 E4-B9-7A-08-C9-EF 001C.7F00.00010\n')
		sys.exit()

def makelist():
	makelist.maclist = []
	for i in sys.argv:
		makelist.maclist.append(i)
	makelist.maclist = makelist.maclist[1:None]

def maclookup():
	checkarg()
	makelist()
	#print(makelist.maclist)
	URL = "https://api.macvendors.com/"
	data = {}
	for mac in makelist.maclist:
		r = requests.get(url = URL + mac)
		data[mac] = r.text
		time.sleep(1.2)
		# this print for sequential output
		print(mac, '=>' , data[mac])
	# this for loop for one shot output
	#for k in data:
	#	print(k, '=>', data[k])


if __name__ == '__main__':
    maclookup()