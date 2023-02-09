import socket
import sys
import random

host = ''
port = 50500
try:
    p = float(sys.argv[1])
    random.seed(int(sys.argv[2]))
except:
    sys.exit("Please type in right parameters!")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

OCVal = ['+','-','/','*']
def calc(client):
    msg, clientAdd  = client.recvfrom(1024)
    data = msg.decode()
    while data:
        try:
            temp = " ".join(data.split())
            oc,i1,i2 = temp.split(' ')
            if(random.random() <= p):
                print("{} -> dropped".format(temp))
                msg, clientAdd  = client.recvfrom(1024) 
                data = msg.decode()               
            elif(oc not in OCVal):
                message = "620 -1"
                client.sendto(message.encode(),clientAdd)
                msg, clientAdd  = client.recvfrom(1024) 
                data = msg.decode()      
            else:   
                try:
                    int1 = int(i1)
                    int2 = int(i2)
                    if (int2 == 0 and oc =='/'):
                        message = "630 -1"
                        client.sendto(message.encode(),clientAdd) 
                        msg, clientAdd  = client.recvfrom(1024)
                        data = msg.decode()           
                    else:
                        if oc == '+':
                            result = int(int1 + int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.sendto(message.encode(),clientAdd)              
                        elif oc == '-':
                            result = int(int1 - int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.sendto(message.encode(),clientAdd)       
                        elif oc == '*':
                            result = int(int1 * int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.sendto(message.encode(),clientAdd)        
                        else: 
                            result = int(int1 / int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.sendto(message.encode(),clientAdd) 
                        print("{} -> 200 {}".format(data, result))
                        msg, clientAdd  = client.recvfrom(1024)
                        data = msg.decode()              
                except ValueError:
                    message = "630 -1"
                    client.sendto(message.encode(),clientAdd) 
                    msg, clientAdd  = client.recvfrom(1024)
                    data = msg.decode() 
        except Exception as e:
            message = "{}".format(e)
            client.sendto(message.encode(),clientAdd)
            msg, clientAdd  = client.recvfrom(1024) 
            data = msg.decode()             
    client.shutdown(socket.SHUT_RDWR)
    client.close()          

try:
    while True:
        calc(s)
except KeyboardInterrupt:
    s.close()

