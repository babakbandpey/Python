#!/usr/bin/python3

from socket import *

serverName = '127.0.0.1'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentece: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('from server: ', modifiedSentence.decode())
clientSocket.close()
