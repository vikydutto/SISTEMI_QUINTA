import socket
#                       IPV4            UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#socket IPV4 
s.bind(("0.0.0.0", 5000)) #solo sui server

while True:
    dati, ind_client = s.recvfrom(4096) #è la dimensione
    print(f"{dati} ricevuti da {ind_client}")
    #stringa = input("Inserisci una stringa: ")
    #s.sendto(stringa.encode(), ind_client)

    