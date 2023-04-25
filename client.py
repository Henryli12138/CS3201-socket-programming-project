from socket import socket, AF_INET, SOCK_STREAM
clientSocket = socket(AF_INET, SOCK_STREAM)
IPAddress = input('Input IP Address: ')
PortNum = input('Input Port Number: ')
print("IP Address :", IPAddress, "Port Number:", PortNum)
clientSocket.connect((IPAddress, int(PortNum))) #initialize and create TCP socket
print("Connect status: OK")
sentence = 'none'
recvSentence ='none'
def client(): #client function
    print("Enter command: ")
    sentence = input() #command input
    clientSocket.send(sentence.encode()) #send command to the server
    #POST Operation
    if sentence == 'POST':
        print('Enter text:')
        while sentence != '#': #command input loop
            sentence = input()
            clientSocket.send(sentence.encode()) #send command to the server
        recvSentence = clientSocket.recv(4096) #receive data from server
        if recvSentence.decode() == 'server: OK':
            print("OK") #print OK when receving OK
            return client()
    #Read command operation
    elif sentence == 'READ':
        recvSentence = clientSocket.recv(4096)
        print(recvSentence.decode('utf-8'))
        while recvSentence.decode('utf-8') != 'server: #': #printing all the
message from server
            recvSentence = clientSocket.recv(4096)
            print(recvSentence.decode('utf-8'))
        return client()
    #QUIT Command operation
    elif sentence == 'QUIT':
'OK'
recvSentence = clientSocket.recv(4096)
if recvSentence.decode() == 'server: OK':  #close the socket if receive
    clientSocket.close()
    #Error message
    elif(sentence != 'POST') & (sentence != 'READ') & (sentence != 'QUIT'):
        recvSentence = clientSocket.recv(4096)
        if recvSentence.decode() == 'server: ERROR - Command not understood':
            print("ERROR - Command not understood")
            return client()
client() #RUN the fuction
