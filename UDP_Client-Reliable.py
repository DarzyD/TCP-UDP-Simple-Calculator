from socket import *
import sys


serverName = 'localhost'
serverPort = 50500
                                                                                                                                         
file = input
f = open(sys.argv[1], 'r')
lines = f.readlines()

for line in lines:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
                                                                                                                                                                                                                                                                                                    
    clientSocket.sendto(line.encode(),(serverName, serverPort))

    # Receive 1024 bytes of data.                                                                                                                                                      
    resp, address = clientSocket.recvfrom(1024)
    data = resp.decode()
    msg = data.split(' ')
    code = msg[0]
    
    if(code == '200'):
        print("Result is {}".format(msg[1]))
        clientSocket.close() 
    elif(code == '620'):
        print("Error {}: Invalid OC".format(code))
        clientSocket.close() 
    elif(code == '630'):
        print("Error {}: Invalid operands".format(code))
        clientSocket.close()
    else:
        print("Error {}: Exception".format(data))
        clientSocket.close()   
# Close socket connection
      