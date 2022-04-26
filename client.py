import socket
import random
from bot import bot_msg, bot_msg_pdr
from threading import Thread
from datetime import datetime
from colorama import Fore, init

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.RED, Fore.YELLOW, Fore.MAGENTA]

client_color = random.choice(colors)
bot_color = random.choice(colors)

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5002
separator_token = "<SEP>"

client_sockets = set()
s = socket.socket()
print(f'[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...')
s.connect((SERVER_HOST, SERVER_PORT))
print('[+] Conectado.')
name = input('Digite seu nome: ')


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    rec_to_send = to_send.lower()
    if to_send.lower() == '/quit':
        print(f'Ecerrando o chat...')
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f'{client_color} [{date_now}] {name}{separator_token} {to_send} {Fore.RESET}'
    s.send(to_send.encode())
    s.send(bot_msg_pdr(bot_msg(msg=rec_to_send)))


s.close()
