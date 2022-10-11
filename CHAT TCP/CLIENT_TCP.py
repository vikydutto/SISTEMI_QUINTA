import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.119", 5000))

class Reciver(Thread):
    def __init__(self):
        Thread.__init__(self)
        
        self.running = True

    def run(self):
        while self.running:
            msg = s.recv(4096)
            print("\n")
            print(msg.decode())

    def stop(self):
        self.running = False


"""def caricaContatti():
    f = open("Indirizzi.csv", 'r')
    testo = f.readlines()
    for line in testo[1:]:
        splittato = line.split(",")
        splittato[1] = splittato[1].replace("\n", "")
        contatti[splittato[0]] = splittato[1]
    print(contatti)
    f.close()


def cercaContatto(nome):
    for contatto in contatti:
        if contatto == nome:
            return contatti[contatto]
    return """


def main():
    #caricaContatti()
    t1 = Reciver()
    t1.start()

    while True:
        destinatario = input("Inserisci il destinatario: ")
        #ipDestinatario = cercaContatto(destinatario)
        msg = input("Scrivi un messaggio: ")
        msg = msg + "|" + destinatario
        s.sendall(msg.encode())

        if msg == "fine":
            t1.stop()
            t1.join()
            t1.run()
            break


if __name__ == "__main__":
    main()