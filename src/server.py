import socket
import json
import random

#ler perguntas
with open('trivia.json', 'r') as file: 
    perguntas = json.load(file)

#criar socket server
serverPort = 12345
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2) #numero máximo de conexoes = 2 players
    
print("Servidor pronto para receber conexões...")


#FUNÇÃO p/ enviar a pergunta para o cliete 

def enviar_pergunta(clientSocket):
    pergunta = random.choice(perguntas)
    clientSocket.send(json.dumps(pergunta).encode()) #converte para bytes antes de enviar o dado logo te que desconverter quando chegar
    
    
#conexão com o cliente


while True:
    clientSocket, clientAdress = serverSocket.accept()
    print(f"Conexão estabelecida com {clientAdress}")
    
    #enviar perguntas para o cliente
    for _ in range(len(perguntas)):
        enviar_pergunta(clientSocket)
        
    clientSocket.close()