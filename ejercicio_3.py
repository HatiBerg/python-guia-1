# Cree un programa que solicite al usuario un número y determine si el número es primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return False
        return True

def main():
    numero = int(input("Ingrese un número entero: "))

    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

if __name__ == '__main__':
    main()