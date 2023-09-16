import socket
import pygame
import json
from game import Game

# Configurações do socket client
host_ip = socket.gethostbyname(socket.gethostname())
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host_ip, serverPort))

game = Game(clientSocket)

game.run_game()

game.quit_game()
