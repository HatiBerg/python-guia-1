# Escriba un programa que calcule el factorial de un número ingresado por el usuario.

def main():
    numero = int(input("Ingrese un número para calcular el factorial: "))
    factorial = 1

    if numero != 0:
        for i in range(1, numero+1):
            factorial = factorial * i

    print(f"El factorial de {numero} es: {factorial}")

if __name__ == '__main__':
    main()