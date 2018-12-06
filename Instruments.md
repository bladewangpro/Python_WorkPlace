### Instruments

> At first, After downloading the Paxos folder from Github. We need put this folder (Paxos folder) under the path  C:\Python_WorkPlace. Because in this project, we use **absolute path** to find folders. 

##### Scenario:

1. Single computer, 2 proposers and 3 acceptors

```shell
python C:\Python_WorkPlace\Paxos\test.py
proposer amount = 2
acceptor amount = 3
Proposers
IP：local ip    Port: 53332    Value: 53332    location: C:\Python_WorkPlace\Paxos\PROPOSER.py
IP：local ip    Port: 53333    Value: 53333    location: C:\Python_WorkPlace\Paxos\PROPOSER.py
Acceptors
IP：local ip    Port: 53334    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
IP：local ip    Port: 53335    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
IP：local ip    Port: 53336    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
```

2. Single computer, 2 proposers and 4 acceptors. 

**We let one acceptor offline in halfway.**

```shell
python C:\Python_WorkPlace\Paxos\test.py
proposer amount = 2
acceptor amount = 4
Proposers
IP：local ip    Port: 53332    Value: 53332    location: C:\Python_WorkPlace\Paxos\PROPOSER.py
IP：local ip    Port: 53333    Value: 53333    location: C:\Python_WorkPlace\Paxos\PROPOSER.py
Acceptors
IP：local ip    Port: 53334    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
IP：local ip    Port: 53335    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
IP：local ip    Port: 53336    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
IP：local ip    Port: 53337    location: C:\Python_WorkPlace\Paxos\ACCEPTOR.py
```

3. Two computer, A computer: 3 acceptors, B computer: 3 learners and 3 proposers.

<u>Before we start to test project between multiple machines, we need shut down the firewall of each computers. We also need write all the IP and Port of acceptors into the log file and all the IP and Port of learners into the learnerLog file.</u>

```shell
Computer a:
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52322
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52320
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52321

Computer b:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53320
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53321
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53322

Computer a:
python C:\Python_WorkPlace\Paxos\PROPOSER.py 78 local_ip 53334
python C:\Python_WorkPlace\Paxos\PROPOSER.py 89 local_ip 53335
python C:\Python_WorkPlace\Paxos\PROPOSER.py 58 local_ip 53336
```



4. Two computer, A computer: 3 acceptors, B computer: 3 learners and 3 proposers.

**We let one acceptor offline in halfway**

<u>Before we begin test our program, we need write all the IP and Port of acceptors into the log file and all the IP and Port of learners into the learnerLog file.</u>

```shell
Computer a:
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52322
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52320
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52321

Computer b:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53320
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53321
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53322

Computer a:
python C:\Python_WorkPlace\Paxos\PROPOSER.py 78 local_ip 53334
python C:\Python_WorkPlace\Paxos\PROPOSER.py 89 local_ip 53335
python C:\Python_WorkPlace\Paxos\PROPOSER.py 58 local_ip 53336
```

5. Three computers, each computer: 1 acceptor, 1 proposer, 1 learner (simulate Three-Army problem)

<u>Before we begin test our program, we need write all the IP and Port of acceptors into the log file and all the IP and Port of learners into the learnerLog file.</u>

```shell
Computer a:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 52320
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52321
python C:\Python_WorkPlace\Paxos\PROPOSER.py 78 local_ip 52322

Computer b:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53321
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 53322
python C:\Python_WorkPlace\Paxos\PROPOSER.py 23 local_ip 53320

Computer c:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53335
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 53336
python C:\Python_WorkPlace\Paxos\PROPOSER.py 22 local_ip 53334
```

6. Three computers, each computer: 1 acceptor, 1 proposer, 1 learner (simulate Three-Army problem)

**We just shut down one acceptor in halfway.**

<u>Before we begin test our program, we need write all the IP and Port of acceptors into the log file and all the IP and Port of learners into the learnerLog file.</u>

```shell
Computer a:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 52320
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 52321
python C:\Python_WorkPlace\Paxos\PROPOSER.py 78 local_ip 52322

Computer b:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53321
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 53322
python C:\Python_WorkPlace\Paxos\PROPOSER.py 23 local_ip 53320

Computer c:
python C:\Python_WorkPlace\Paxos\ACCEPTOR.py local_ip 53335
python C:\Python_WorkPlace\Paxos\LEARNER.py local_ip 53336
python C:\Python_WorkPlace\Paxos\PROPOSER.py 22 local_ip 53334
```