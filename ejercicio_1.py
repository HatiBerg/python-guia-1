# Cree un programa que elija un numero al azar entre 1 y 100, luego le pregunta por un número y el programa le debe decir si 
# el numero ingresado es demasiado bajo o demasiado alto, hasta que logre dar con el numero generado.

import random

def main():
    numero_random = random.randint(1,100)
    numero = int(input("Ingrese un número: "))
    #print(f"Número random: {numero_random}") #Testing

    while(numero != numero_random):
        if numero > numero_random:
            print("El numero ingresado es demasiado alto")
        if numero < numero_random:
            print("El numero ingresado es demasiado bajo")
        numero = int(input("Ingrese un número: "))

    print("Encontraste el numero generado aleatoriamente")
    print(f"Número random: {numero_random}")

if __name__ == '__main__':
    main()