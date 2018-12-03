"""
	@author: Tianyi Wang

	@file: test.py

	@time: Nov 2018

	@function: test the paxos protocol python program
"""

import socket
import os


from PROPOSER import PROPOSER
from ACCEPTOR import ACCEPTOR
import sf

if __name__ == '__main__':

	gui = sf.GUI()


	#ip_acceptor = '192.168.1.65'
	#ip_proposer = '192.168.1.65'

	#acceptors = [(ip_acceptor, port) for port in range(65520, 65526)]
	acceptors = []
	buffer = [1]*3
	for i in range(len(gui.acceptorIP)):
		buffer[0] = gui.acceptorIP[i]
		buffer[1] = gui.acceptorPort[i]
		buffer[2] = gui.acceptorLoc[i]
		acceptors.append(buffer[:])

	fileHandle = open('log', 'w')
	for k in acceptors:
		fileHandle.write(k[0])
		fileHandle.write('\n')
		z = str(k[1])
		fileHandle.write(z)
		fileHandle.write('\n')
	fileHandle.close()


	#a_p = 65520
	#value = [1, 2, 3, 4, 5]


	for i in range(len(acceptors)):
		#os.system(r"start cmd /k python C:\Users\blade\Downloads\Paxos\ACCEPTOR.py %s %d" % (ip_acceptor, a_p))
		#a_p = a_p + 1
		os.system(r"start cmd /k python %s %s %s" % (acceptors[i][2], acceptors[i][0], acceptors[i][1]))



	for i in range(len(gui.proposerValue)):
		os.system(r"start cmd /k python %s %s %s %s" % (gui.proposerLoc[i] ,gui.proposerValue[i], gui.proposerIP[i], gui.proposerPort[i]))

	#os.system(r"start cmd /k python C:\Users\blade\Downloads\Paxos\PROPOSER.py %d %s %d" % (value[0], ip_proposer, a_p))
	#a_p = a_p + 1
	#os.system(r"start cmd /k python C:\Users\blade\Downloads\Paxos\PROPOSER.py %d %s %d" % (value[2], ip_proposer, a_p))
	#a_p = a_p + 1
	#os.system(r"start cmd /k python C:\Users\blade\Downloads\Paxos\PROPOSER.py %d %s %d" % (value[3], ip_proposer, a_p))
