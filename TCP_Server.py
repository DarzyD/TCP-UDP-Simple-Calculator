import socket

host = ''
port = 50500
backlog = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

OCVal = ['+','-','/','*']
def calc(client,address):
    data = client.recv(1024).decode()
    while data:
        try:
            temp = " ".join(data.split())
            oc,i1,i2 = temp.split(' ')            
            if(oc not in OCVal):
                message = "620 -1"
                print("{} -> 620 -1".format(data))
                client.send(message.encode())
                data = client.recv(1024).decode()      
            else:   
                try:
                    int1 = int(i1)
                    int2 = int(i2)
                    if (int2 == 0 and oc =='/'):
                        message = "630 -1"
                        print("{} -> 630 -1".format(data))
                        client.send(message.encode())
                        data = client.recv(1024).decode()            
                    else:
                        if oc == '+':
                            result = int(int1 + int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.send(message.encode())                
                        elif oc == '-':
                            result = int(int1 - int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.send(message.encode())        
                        elif oc == '*':
                            result = int(int1 * int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.send(message.encode())        
                        else: 
                            result = int(int1 / int2)
                            rs = str(result)
                            message = "200 " + rs
                            client.send(message.encode()) 
                        print("{} -> 200 {}".format(data, result))
                        data = client.recv(1024).decode()            
                except ValueError:
                    message = "630 -1"
                    print("{} -> 630 -1".format(data))
                    client.send(message.encode())
                    data = client.recv(1024).decode()     
        except Exception as e:
            message = "{}".format(e)
            client.send(message.encode())
            data = client.recv(1024).decode()                       

        client.shutdown(socket.SHUT_RDWR)
        client.close()

try:
    while True:
        client, address = s.accept()
        calc(client,address)
except KeyboardInterrupt:
    client.close()


# while True:
#     client, address = s.accept()
#     calc(client,address)