import threading
import time
import random
import sys
import socket

rsHostname = sys.argv[1]
rsListenPort = sys.argv[2]
rsListenPort = int(rsListenPort)
tsListenPort = sys.argv[3]
tsListenPort = int(tsListenPort)

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
    
    # get root server's ip
    # rsHostname is given as argument1 in command line
    rsHostip = socket.gethostbyname(rsHostname)
    print("[C]: root server's host is {} and ip is {}.".format(rsHostname,rsHostip)) 
    
    # client connects to rs host machine
    rootServerBinding = (rsHostname, rsListenPort)
    # connect to root server 
    cs.connect(rootServerBinding)
    
    # domain name list from text file
    lst = []
    # open up file and go through each line, place contents in list called lst
    with open("PROJI-HNS.txt", "r") as f:
        lines = f.readlines()
        #print(lines)
    for line in lines:
        lst.append(line.strip())
    

    #send contents on lst to server
    print("\n")
    for domainName in lst:
        print(domainName) #this helps with sending domainName efficiently. put time instead.
        cs.send(domainName.encode('utf-8'))
   	time.sleep(1) 
	msg_recv = cs.recv(100).decode('utf-8')
	print("[C] Message received from RS Server: {}".format(msg_recv))
    cs.send("0".encode('utf-8'))	
    time.sleep(10)
    msg = cs.recv(1024).decode('utf-8')
    print("[C] {}".format(msg))
    #receive message from server after sending domain names to server
    #to salman abu khan, this is where the test message should be received, but isn't.
    #after we can implement receiving one message back from the root server, then we can 
    #implement receiving multiple messages which would be the return strings hostname ip flag if exists
    #and other return string format if flag is NS
    
    #cs.send("hey from client".encode('utf-8'))
    #msg_recv = cs.recv(1024)
    #time.sleep(1)
    #print("[C] Message from server: {}".format(msg_recv.decode('utf-8')))
         
if __name__ == "__main__":
    #t1 = threading.Thread(name='server', target=server)
    #t1.start()

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    #time.sleep(40)
    print("Done.")
    
