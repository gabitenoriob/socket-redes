import socket
import threading 
import pygame
import json

# configurações do socket client 
serverName = 'servername'
serverPort = 12345
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# codigo py game 

pygame.init()

#tela
WIDTH, HEIGHT =  800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trivia")
WHITE=(255,255,255)
BLACK=(0,0,0)
FONT = pygame.font.Font("C:\Users\gabit\Downloads\04b_30\04B_30__.TTF",36)

#FUNCAO exibir a pergunta 
def display_pergunta():
    texto_pergunta = FONT.render(pergunta_atual['pergunta'], True, BLACK)
    SCREEN.blit(texto_pergunta(50,50))
    
#FUNCAO enviar RESPOSTA

def enviar_resposta(resposta):
    clientSocket.send(resposta.encode())
    
#nova pergunta

def atualizar_pergunta():
    pergunta = clientSocket.recv(1024).decode()
    if not pergunta:
        clientSocket.close()
        pygame.quit()
        quit()
    else:
        global pergunta_atual
        pergunta_atual = json.loads(pergunta)
        display_pergunta()
        
    pergunta_atual= None

    
    running = True
    
    while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        
                    elif event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_a:
                         enviar_resposta('A')
                         atualizar_pergunta()
                        elif event.key == pygame.K_b:
                            enviar_resposta('B')
                            atualizar_pergunta()
                        elif event.key == pygame.K_c:
                            enviar_resposta('C')
                            atualizar_pergunta()
                        elif event.key == pygame.K_d:
                            enviar_resposta('D')
                            atualizar_pergunta()
        
                    pygame.display.flip()
        
    pygame.quit()



