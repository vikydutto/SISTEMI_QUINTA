def main():
    numero = int(input("Inserisci un numero: "))
    if numero > 1:
        isPrimo(numero)
    else:
        print("Inserire un numero positivo e maggiore di !!") 

def isPrimo(numero):
            controllo = False
            cont = 2
            while cont < int(numero**0.5)+1 and controllo == False:
                n = numero % cont
                if n == 0:
                    controllo = True ##se è true esce 
                    print("{numero} non è un numero primo")
                
                cont += 1
            
            if controllo == False:
                print("{numero} è un numero primo")   

if __name__ == "__main__":
    main()