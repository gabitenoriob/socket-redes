import socket
import json
import random

#ler perguntas
with open('trivia.json', 'r') as file: 
    perguntas = json.load(file)

#criar socket server
serverPort = 12000
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
    jogador1_pontuacao = 0
    jogador2_pontuacao = 0
    jogador1_socket, jogador1_adress = serverSocket.accept()
    print(f"Jogador 1 conectado: {jogador1_adress}")
    jogador2_socket, jogador2_adress = serverSocket.accept()
    print(f"Jogador 2 conectado: {jogador2_adress}")

    for _ in range(len(perguntas)): 

        enviar_pergunta(jogador1_socket)
        enviar_pergunta(jogador2_socket)

        # pegar respostas
        resposta_jogador1 = jogador1_socket.recv(1024).decode()
        resposta_jogador2 = jogador2_socket.recv(1024).decode()

        # verificar e somar pontos
        pergunta_atual = perguntas[_]
        if resposta_jogador1.lower() == pergunta_atual['resposta'].lower():
            jogador1_pontuacao += 1
        if resposta_jogador2.lower() == pergunta_atual['resposta'].lower():
            jogador2_pontuacao += 1

    # pontuações finais 
    jogador1_socket.send(f"Sua pontuação final: {jogador1_pontuacao}".encode())
    jogador2_socket.send(f"Sua pontuação final: {jogador2_pontuacao}".encode())

    
    jogador1_socket.close()
    jogador2_socket.close()