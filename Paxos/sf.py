"""
	@author: Tianyi Wang && Wensong Xiao

	@file: ACCEPTOR.py

	@time: Nov 2018

	@function: GUI 
"""

from tkinter import *



class GUI:
	def __init__(self):
		self.root = Tk()
		self.root.title('Paxos')
		#self.root.iconbitmap(r'C:\Python_WorkPlace\Paxos\1.ico')
		self.root.geometry('300x200')
		Label(self.root,text='\n\n\n').grid(row=1,column=0)
		Label(self.root,text='      proposer amount:').grid(row=3,column=0)
		Label(self.root,text='      acceptor amount:').grid(row=6,column=0)

		self.e1 = Entry(self.root,textvariable=StringVar()) 
		self.e2 = Entry(self.root,textvariable=StringVar())

		self.e1.grid(row=3,column=1,padx=10,pady=5)
		self.e2.grid(row=6,column=1,padx=10,pady=5)

		self.proposerValue = []
		self.proposerIP = []
		self.proposerPort = []
		self.proposerLoc = []

		self.acceptorIP = []
		self.acceptorPort = []
		self.acceptorLoc = []


		def enter():
			

			self.proposers = [1] * int(self.e1.get())
			self.acceptors = [1] * int(self.e2.get())

			self.num_proposers = int(self.e1.get())
			self.num_acceptors = int(self.e2.get())

			self.win0 = Tk()
			self.win0.title('Proposers')
			#self.win0.iconbitmap(r'C:\Python_WorkPlace\Paxos\1.ico')
			self.win0.geometry('%s%s%s' % (str(800), 'x', str(self.num_proposers * 29 + 40)))
			for i in range(0,int(self.e1.get())):
				#IP
				Label(self.win0,text='IP:').grid(row=i+2,column=0)
				self.proposerIP.append(Entry(self.win0,textvariable=StringVar()))
				self.proposerIP[i].grid(row=i+2,column=1,padx=10,pady=5)

				Label(self.win0,text='Port:').grid(row=i+2,column=2)
				self.proposerPort.append(Entry(self.win0,textvariable=StringVar()))
				self.proposerPort[i].grid(row=i+2,column=3,padx=10,pady=5)

				Label(self.win0,text='Value:').grid(row=i+2,column=4)
				self.proposerValue.append(Entry(self.win0,textvariable=StringVar()))
				self.proposerValue[i].grid(row=i+2,column=5,padx=10,pady=5)

				Label(self.win0,text='Location:').grid(row=i+2,column=6)
				self.proposerLoc.append(Entry(self.win0,textvariable=StringVar()))
				self.proposerLoc[i].grid(row=i+2,column=7,padx=10,pady=5)
				
			def test():
				for m in range (len(self.proposerIP)):
					self.proposerIP[m] = self.proposerIP[m].get()
					self.proposerPort[m] = self.proposerPort[m].get()
					self.proposerValue[m] = self.proposerValue[m].get()
					self.proposerLoc[m] = self.proposerLoc[m].get()
					print('self.proposerIP: %s' % self.proposerIP[m])
					print('self.proposerPort: %s' % self.proposerPort[m])
					print('self.proposerValue: %s' % self.proposerValue[m])
					print('self.proposerLoc: %s' % self.proposerLoc[m])

				#next page
				self.win1 = Tk()
				self.win1.title('Acceptors')
				#self.win1.iconbitmap(r'C:\Python_WorkPlace\Paxos\1.ico')
				self.win1.geometry('%s%s%s' % (str(600), 'x', str(self.num_acceptors * 29 + 40)))

				for i in range(0,int(self.e2.get())):
					#IP
					Label(self.win1,text='IP:').grid(row=i+2,column=0)
					self.acceptorIP.append(Entry(self.win1,textvariable=StringVar()))
					self.acceptorIP[i].grid(row=i+2,column=1,padx=10,pady=5)

					Label(self.win1,text='Port:').grid(row=i+2,column=2)
					self.acceptorPort.append(Entry(self.win1,textvariable=StringVar()))
					self.acceptorPort[i].grid(row=i+2,column=3,padx=10,pady=5)

					Label(self.win1,text='Location:').grid(row=i+2,column=4)
					self.acceptorLoc.append(Entry(self.win1,textvariable=StringVar()))
					self.acceptorLoc[i].grid(row=i+2,column=5,padx=10,pady=5)

				def submitAcc():
					for m in range (len(self.acceptorIP)):
						self.acceptorIP[m] = self.acceptorIP[m].get()
						self.acceptorPort[m] = self.acceptorPort[m].get()
						self.acceptorLoc[m] = self.acceptorLoc[m].get()
						print('self.acceptorIP: %s' % self.acceptorIP[m])
						print('self.acceptorPort: %s' % self.acceptorPort[m])
						print('self.acceptorLoc: %s' % self.acceptorLoc[m])
					
					
					self.root.destroy()
					self.win0.destroy()
					self.win1.destroy()
					
					
				Button(self.win1,text='Go',width=10,command=submitAcc).grid(row=self.num_acceptors + 2 ,column=5,sticky=W,padx=10,pady=5)

			Button(self.win0,text='Next',width=10,command=test).grid(row=self.num_proposers + 2 ,column=7,sticky=W,padx=10,pady=5)




		Button(self.root,text='Enter',width=10,command=enter).grid(row=10,column=1,sticky=W,padx=10,pady=5)
		mainloop()







		