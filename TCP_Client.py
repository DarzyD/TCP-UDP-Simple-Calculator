from socket import *
import sys

# Get the server hostname and port as command line arguments
serverName = 'localhost'
serverPort = 50500
                                                                                                                                         
file = input
f = open(sys.argv[1], 'r')
lines = f.readlines()

for line in lines:
    #connecting to server
    clientSocket = socket(AF_INET, SOCK_STREAM)                                                                                                                           
    clientSocket.connect((serverName, serverPort))
 
    # Send the data to the server                                                                                                                                                      
    clientSocket.send(line.encode())

    # Receive 1024 bytes of data.                                                                                                                                                      
    resp = clientSocket.recv(1024)
    data = resp.decode()
    msg = data.split(' ')
    code = msg[0]
    #close server connection
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