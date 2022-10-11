def main():
    n = 991847
    f = open("Num_primi.txt", "r")
    righe = f.readlines()
    numeri = []
    for riga in righe:
        numeri.append(int(riga))
    
    fattoriPrimi(n, numeri)
    

def fattoriPrimi(numero, lista):
    fattori = []

    for x in lista:
        if numero % x == 0:
            fattori.append(x)
    
    print(f"il primo fattore è {fattori[0]} e il secondo è {fattori[1]}")

if __name__ == "__main__":
    main()