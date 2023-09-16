import socket
import json

serverPort = 12345
serverSocket= socket(AF_INIT, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(2)


#enviar a pergunta para o cliete 
