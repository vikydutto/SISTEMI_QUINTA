import socket
import string

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    stringa = input("Inserisci una stringa: ")
    s.sendto(stringa.encode(), ("192.168.0.137", 5000))

