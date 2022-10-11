def main():
    f = open("Num_primi.txt", "w")

    for x in range (2, 100000):
        if isPrimo(x) == False:
            f.write(f"{x}\n")
    f.close()


def isPrimo(numero):
            controllo = False
            cont = 2
            while cont < int(numero**0.5)+1 and controllo == False:
                n = numero % cont
                if n == 0:
                    controllo = True ##se è true esce                
                cont += 1
            return controllo


if __name__ == "__main__":
    main()