# Escriba un programa que pida al usuario una palabra y la imprima al revés. El programa debe
# continuar pidiendo palabras hasta que el usuario ingrese "salir";.

def main():
    palabra = input("Ingrese una palabra: ")
    while(palabra.lower() != "salir"):
        print(f"Palabra normal: {palabra.lower()}")
        print(f"Palabra al revés: {palabra[::-1].lower()}")
        palabra = input("Ingrese una palabra: ")
    print("Programa terminado")

if __name__ == '__main__':
    main()