def primeraUltima(palabra):
    primera = palabra[0]
    ultima = palabra[len(palabra) - 1]
    primul = primera +" "+ ultima;
    return primul;

def main():
    palabra = input("Por favor ingrese una palabra: ")
    print("La primera y la última letra de su palabra son respectivamente: ", primeraUltima(palabra))

if __name__ == '__main__':
    main()