"""
	@author: Tianyi Wang && Wensong Xiao

	@file: PROPOSER.py

	@time: Nov 2018

	@function: simulate the proposers in Paxos protocol
"""

import socket
import sys
import json
import random
import time

class PROPOSER:

	#Intialization
	def __init__(self, value, ip = None, port = None, acceptors = None, learners = None):



		if acceptors == None:
			self.acceptors = []
		else:
			self.acceptors = acceptors

		if ip != None:
			self.ip = ip
		if port != None:
			self.port = int(port)


		self.proposalID = 0	#Used to get winning in the first round

		self.run = False

		self.soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		self.soc.bind((self.ip, self.port))
		self.agreeCount = 0
		self.rejectCount = 0

		self.phase1Sign = 0

		self.acceptStatus = -1		#not yet	
		self.dicidedStatus = -1	#not yet
		self.value = value
		self.acceptorArray = []
		self.halfNum = len(acceptors)/2

		self.changingList = []

	def stop(self):
		self.run = False

	def getHalfNum(self):
		return len(acceptors)/2


	def getLearners(self):
		return self.learners

	def getAcceptors(self):
		return self.acceptors

	def broadcast(self):
		print('broadcast %s\n' % self.value)
		f0 = open(r'C:\Python_WorkPlace\Paxos\learnerLog', 'r')
		learnerArr = []
		i = 0
		i_tuple = [1]*2
		for line in f0.readlines():
			a = i_tuple[:]
			if i == 2:
				learnerArr.append(a)
				i = 0
			i_tuple[i] = line.strip()
			i = i + 1
		learnerArr.append(i_tuple)
		f0.close()

		for i in learnerArr:
			message = {
				'status': 'broadcast',
				'value': self.value
			}
			message = json.dumps(message)
			proposer.soc.sendto(message.encode('utf-8'), (i[0], int(i[1])))

#initialize the Proposer program
if len(sys.argv)==1:
	pass
else:
	
	#ip = '192.168.1.65'
	#acceptors = [(ip, port) for port in range(65520, 65525)]
	f = open(r'C:\Python_WorkPlace\Paxos\log', 'r')
	acceptors = []
	i = 0
	i_tuple = [1]*2
	for line in f.readlines():
		a = i_tuple[:]
		if i == 2:
			acceptors.append(a)
			i = 0
		i_tuple[i] = line.strip()
		i = i + 1
	acceptors.append(i_tuple)
	f.close()

	for i in acceptors:
		print("%s %s" % (i[0], i[1]))


	proposer = PROPOSER(sys.argv[1], sys.argv[2], sys.argv[3], acceptors)	#ip and port

	proposer.proposalID = proposer.proposalID + random.randint(0,100)
	while proposer.phase1Sign == 0:

		#simulate the delay in network environment 
		time.sleep(random.randint(0, 10))

		for server in proposer.getAcceptors():
			message = {
				'proposalID': proposer.proposalID,
				'proposalValue': proposer.value,
				'phase1Sign': proposer.phase1Sign,
				'stop': 'None'
			}

			message = json.dumps(message)
			proposer.soc.sendto(message.encode('utf-8'), (server[0], int(server[1])))
			time.sleep(random.randint(0, 2))

		while (proposer.agreeCount <= proposer.halfNum) and (proposer.rejectCount <= proposer.halfNum):
			try: 
				data, addr = proposer.soc.recvfrom(1024)
				data = data.decode('utf-8')
				m = json.loads(data)
				print('p1111111111111--------------[dicidedValue: %s, proposalID: %s, acceptStatus: %s]\n' % (m['dicidedValue'], m['proposalID'], m['acceptStatus']))


				if m['acceptStatus'] == 1:
					proposer.agreeCount = proposer.agreeCount + 1
					proposer.acceptorArray.append(addr)					
				elif m['acceptStatus'] == 0:
					proposer.rejectCount = proposer.rejectCount + 1
				else:
					print('^^^^^^^^^^^^^^^^^^^^ %s' % m['acceptStatus'])
			except socket.error:
				proposer.rejectCount = proposer.rejectCount + 1
				
			

		if proposer.agreeCount > proposer.halfNum:
			print("Proposer whose ID is %s pass the first phase\n" % proposer.proposalID)
			#Second phase
			proposer.phase1Sign = 1

			for server in proposer.acceptorArray:
				message = {
					'proposalID': proposer.proposalID,
					'proposalValue': proposer.value,
					'phase1Sign': proposer.phase1Sign,
					'stop': 'None'
				}
				message = json.dumps(message)
				proposer.soc.sendto(message.encode('utf-8'), (server[0], server[1]))
				time.sleep(random.randint(0, 2))
			proposer.agreeCount, proposer.rejectCount = 0, 0

			while (proposer.agreeCount <= proposer.halfNum) and (proposer.rejectCount <= proposer.halfNum):
				print('-----------------------------')
				
				try: 
					print('proposer.agreeCount = %d, proposer.rejectCount = %d' % (proposer.agreeCount, proposer.rejectCount))
					proposer.soc.settimeout(15.00)
					data, addr = proposer.soc.recvfrom(1024)
					data = data.decode('utf-8')
					m = json.loads(data)
					print('[dicidedValue: %s, proposalID: %s, acceptStatus: %s]' % (m['dicidedValue'], m['proposalID'], m['acceptStatus']))

					if m['acceptStatus'] == 2:
						proposer.agreeCount = proposer.agreeCount + 1
					elif m['acceptStatus'] == 3:
						#proposer.value = m['dicidedValue']
						proposer.changingList.append(m['dicidedValue'])
						print('----------------------%s' % proposer.value)
						proposer.agreeCount = proposer.agreeCount + 1
					elif m['acceptStatus'] == 0:
						proposer.rejectCount = proposer.rejectCount + 1
					else:
						print('&&&&&&&&&&&&&&&&&&& %s' % m['acceptStatus'])
				except socket.error:
					proposer.rejectCount = proposer.rejectCount + 1
				except socket.timeout:
					proposer.agreeCount = 0
					proposer.rejectCount = 0
					break


			if proposer.agreeCount > proposer.halfNum:
				print("agreeCount: %s halfNum: %s" %(proposer.agreeCount, proposer.halfNum))
				print('len(proposer.changingList = %d): ' % len(proposer.changingList))
				if len(proposer.changingList) != 0:
					dic = {}
					for k in proposer.changingList:
						dic[k] = dic.get(k, 0) + 1
					proposer.value = sorted(dic.keys(), reverse = True)[0]
				proposer.broadcast()
			else:
				proposer.phase1Sign = 0
			proposer.changingList = []
			proposer.acceptorArray = []

		else:
			print("Proposer whose ID is %s does not pass the first phase and need restart the first phase.\n" % proposer.proposalID)
			proposer.agreeCount = 0
			proposer.rejectCount = 0
			proposer.proposalID = proposer.proposalID + random.randint(0,100)
