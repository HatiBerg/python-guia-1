# Escribir un programa que contenga una función que reciba una lista de palabras y devuelva la
# palabra más larga. Imprimir por pantalla la palabra resultante.

def palabra_larga(lista):
    palabra_larga = ""
    palabra_longitud = 0
    for palabra in lista:
        if palabra_longitud < len(palabra):
            palabra_longitud = len(palabra)
            palabra_larga = palabra
    return palabra_larga

def main():
    lista = ["Hola", "Casa", "Volumen", "Area", "Tigre", "Paralelepípedo", "Cilindro", "Circulo"]
    print(f"La palabra más larga es {palabra_larga(lista)} y esta tiene {len(palabra_larga(lista))} letras")

if __name__ == '__main__':
    main()