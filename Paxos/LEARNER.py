"""
	@author: Tianyi Wang

	@file: LEARNER.py

	@time: Nov 2018

	@function: initialize the Learner program
"""
import sys
import json
import socket

class LEARNER:

	#Intialization
	def __init__(self, ip, port):
		self.ip = ip
		self.port = int(port)
		
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind((self.ip, self.port))

		self.value = -1
		
		data, addr = self.s.recvfrom(1024)
		data =data.decode('utf-8')
		result = json.loads(data)
		if result['status'] == 'broadcast':
			#show
			self.value = result['value']
			print('DecideValue is %s' % result['value'])
			

learner = LEARNER(sys.argv[1], sys.argv[2])