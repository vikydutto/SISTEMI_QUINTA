import socket
from threading import Thread


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class receiver(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        self.s = s
        self.running = Trung

    def run(self):
        while self.running:
            dati, ind_client = self.s.recvfrom
