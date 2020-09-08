def parImpar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    num = int(input("Ingrese un número entero: "))
    print(parImpar(num))

if __name__ == '__main__':
    main()