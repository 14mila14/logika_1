from socket import *
import threading
from colorama import Fore, Style, init


init()


client_socket = socket(AF_INET, SOCK_STREAM)# TCP
name = input('Введіть нікнейм: ')


try:
    client_socket.connect(('4.tcp.eu.ngrok.io', 15895))
except Exception as e:
    print(f'Не вийшло доєднатись: {e}')
    exit()


client_socket.send(name.encode())


print('Ви в чаті! Щоб вийти наниши `exit` '+ Fore.GREEN)


def send_message():
    while True:
        message = input('>>' + Fore.CYAN)
        if message.lower() == 'exit':
            client_socket.send(f'{name} покинув чат'.encode())
            client_socket.close()
            break
        client_socket.send(message.encode())


threading.Thread(target=send_message).start()


while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(Fore.BLUE + f'\n {message}' + Style.RESET_ALL)
    except:
        print(Fore.RED + '\n Зв`язок обірвано.')
        break