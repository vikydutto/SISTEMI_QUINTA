import socket
#                       IPV4            UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#socket IPV4 
s.bind(("0.0.0.0", 5000)) #solo sui server
print("connesso")
ass_nomi = {}

f = open("./ip.csv", "r")
righe = f.readlines()
for riga in righe:
    print(riga)
    campi = riga.split(",")
    ass_nomi[campi[0]] = campi[1][:-1]

f.close()

while True:
    dati, ind_client = s.recvfrom(4096) #è la dimensione
    print(f"{dati.decode()} ricevuti da {ind_client}")
    
    dati = dati.decode()
    messaggio, dest = dati.split("|")[0], dati.split("|")[1]
    for nome in ass_nomi:
        if nome == dest:
            ip = (ass_nomi[nome], 5000)
    
        s.sendto(messaggio.encode(), ip)