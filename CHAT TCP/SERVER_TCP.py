from http import server
import socket
from sqlite3 import connect
from threading import Thread

contatti = {}
connessioni = {}


class ServerThread(Thread):
    def __init__(self, connection):
        Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            message = (self.connection.recv(4096).decode())
            #trovare il messaggio e il nick
            #dal nick ottengo l'ip
            #salvare tutte le connection
            #message = message.split("|")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0"), 5000)
    sock.listen()
    caricaContatti()
    while True:
        connect, address = sock.accept()
        t = ServerThread(connect)
    
    t = ServerThread()
    t.start()

if __name__ == "__main__":
    main()
