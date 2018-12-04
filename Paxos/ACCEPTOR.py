"""
	@author: Tianyi Wang

	@file: ACCEPTOR.py

	@time: Nov 2018

	@function: initialize the Acceptor program
"""
import sys
import json
import socket

class ACCEPTOR:

	#Intialization
	def __init__(self, ip, port, proposers = None):
		self.ip = ip
		self.port = int(port)
		if proposers == None:
			self.proposers = []
		else:
			self.proposers = proposers
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind((self.ip, self.port))
		self.proposalID = -1
		self.reserveValue = -1
		self.acceptStatus = 0
		self.dicidedStatus = 0

	def start(self):
		while True:
			data, addr = self.s.recvfrom(1024)
			data =data.decode('utf-8')
			result = json.loads(data)
			#if result['stop'] == 'stop':
			#	break
			#debug
			print('[phase1Sign: %s, proposalID: %s, proposalValue: %s]' % (result['phase1Sign'], result['proposalID'], result['proposalValue']))

			if self.reserveValue == -1:
				if result['phase1Sign'] == 0:
					if result['proposalID'] <= self.proposalID:#reject
						self.acceptStatus = 0
					else:
						self.acceptStatus = 1
						self.proposalID = result['proposalID']
				else:
					if result['proposalID'] == self.proposalID:
						self.acceptStatus = 2 #已经决定
						self.reserveValue = result['proposalValue']
					else:
						self.acceptStatus = 0
			else:
				if result['phase1Sign'] == 0:
					if result['proposalID'] <= self.proposalID:#reject
						self.acceptStatus = 0
					else:
						self.acceptStatus = 1
						self.proposalID = result['proposalID']
				else:
					if result['proposalID'] >= self.proposalID:
						self.proposalID = result['proposalID']
						self.acceptStatus = 3
					else:
						self.acceptStatus = 0

			m = {
				'proposalID': self.proposalID,
				'dicidedValue': self.reserveValue,
				'acceptStatus': self.acceptStatus,
			}
			print('------acceptStatus: %s; proposalID: %s; dicidedValue: %s' % (self.acceptStatus, self.proposalID, self.reserveValue))
			m = json.dumps(m)
			self.s.sendto(m.encode('utf-8'), addr)
			self.acceptStatus = 0

#initialize the Acceptor program
if len(sys.argv)==1:
	#print('Hello World')
	pass
else:
	acceptor = ACCEPTOR(sys.argv[1], sys.argv[2])	#ip and port
	acceptor.start()
