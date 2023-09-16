import socket
import threading 
import pygame
import json


serverName = 'servername'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# codigo py game 



#enviar resposta ao servidor e fechar jogo E cliente 
clientSocket.close()

