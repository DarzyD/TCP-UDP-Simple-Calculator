from socket import *
import sys



serverName = 'localhost'
serverPort = 50500
                                                                                                                                         
f = open(sys.argv[1], 'r')
lines = f.readlines()

codeTemp = '0'

for line in lines:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
                                                                                                                                                                                                                                                                                                    
    clientSocket.sendto(line.encode(),(serverName, serverPort))
    d = 0.1
    # Start the timer. 
    clientSocket.settimeout(d)
    resp = None
    address = None
    while (resp == None) and (address == None):
        try:        
            resp, address = clientSocket.recvfrom(1024)
        except:
            d *= 2
            try:
                if(d > 2):
                    codeTemp = '300'
                    raise Exception("Request timed out: the server is dead")
                else:
                    print("Request timed out: resending")
                    clientSocket.sendto(line.encode(),(serverName, serverPort))
                    clientSocket.settimeout(None)
                    clientSocket.settimeout(d)
                    continue
            except:
                print("Request timed out: the server is dead")
                break

    if(codeTemp == '300'):
        print("Error {}: The server is dead!".format(codeTemp))
        codeTemp = '0'
        clientSocket.close()
    else:
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