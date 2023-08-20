# Escribe un programa que le pida al usuario una palabra y una letra. El programa debe contar
# cuántas veces aparece la letra en la palabra usando un ciclo for.

def main():
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese una letra: ")
    cont = 0

    for i in palabra:
        if (letra.lower() == i.lower()):
            cont+=1

    print(f"Veces que se repite la letra {letra} en la palabra {palabra}: {cont}")

if __name__ == '__main__':
    main()