#Entrambe le persone devono avere una chiave
# chiave = stringa
#la parola da decodificare deve essere più corta della chiave
#chiave: "itisdelpozzo"

#ogni lettera corrisponde ad un numero
# a:0 b:1  c:2  d:3  e:4   f:5   g:6...
# il dizionario inverso lo calcolo
# 
# parola: "ciao" 
# 
# 

chiave = "itisdelpozzo"
parola = "ciao"

diz_char_num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'l':9, 'm':10, 'n':11, 'o':12, 'p':13, 'q':14, 'r':15, 's':16, 't':17, 'u':18, 'v':19, 'z':20}  
diz_num_char = {}



for element in diz_char_num:
    diz_num_char[diz_char_num[element]] = element

def numerata(string):
    #string corrisponde alla chiave
    list = []
    trasformato = []

    for carattere in string:
        list.append(carattere)
    
    for element in list:
        trasformato.append(diz_char_num[element])
    
    return trasformato

def codifica(chiave_cod, parola_cod,diz_num_char):
    num_to_char = []
    lettere_cod = []
    string = ""

    for element1, element2 in zip(chiave_cod, parola_cod):
        somma = 0
        somma = somma + element1 + element2
        somma = somma % 21
        num_to_char.append(somma)
    
    #num_to_char contiene la somma con il %21 

    for element in num_to_char:
        lettere_cod.append(diz_num_char(element))

    for element in lettere_cod:
        string = string + element

    return element


chiave_cod = numerata(chiave)
parola_cod = numerata(parola)

cod = codifica(chiave_cod, parola_cod, diz_num_char)
print(cod)





