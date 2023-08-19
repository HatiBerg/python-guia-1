# Cree un programa que elija un numero al azar entre 1 y 100, luego le pregunta por un número y el programa le debe decir si 
# el numero ingresado es demasiado bajo o demasiado alto, hasta que logre dar con el numero generado.

import random

numero_random = random.randint(1,100)

while(True):
    numero = int(input("Ingrese un número: "))
    if numero > numero_random:
        print("El numero ingresado es demasiado alto")
    elif numero < numero_random:
        print("El numero ingresado es demasiado bajo")
    else:
        print("Encontraste el numero generado aleatoriamente")
        break