# Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las últimas tres
# letras tiene que decir que riman. Si coinciden sólo las últimas dos tiene que decir que riman un
# poco. Y si no coinciden, decir que no riman. Validar que las palabras tengan al menos tres letras.
# Nota: Utilizar slices.

def main():
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")

    if len(palabra1) < 3 or len(palabra2) < 3:
        print("ERROR: Las palabras tiene que tener tres letras o más.")
    else:
        if palabra1[-3:] == palabra2[-3:]:
            print("Las palabras riman.")
        elif palabra1[-2:] == palabra2[-2:]:
            print("Las palabras riman un poco.")
        else:
            print("Las palabras no riman.")

if __name__ == '__main__':
    main()