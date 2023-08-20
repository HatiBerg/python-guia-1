# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
# debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida
# terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el
# siguiente formato:

def main():
    lista_compra = {}
    total = 0
    print("LISTA DE COMPRA")
    print("ESCRIBA TERMINAR PARA FINALIZAR LA LISTA DE COMPRA")
    articulo = input("Ingrese el nombre del artículo: ")
    
    while(articulo.lower() != "terminar"):
        precio = int(input("Ingrese el precio del artículo: "))
        lista_compra[articulo] = precio
        print("")
        articulo = input("Ingrese el nombre del artículo: ")
    print("")

    if len(lista_compra) == 0:
        print("La lista de compra esta vacía")
    else:
        print("Lista de compra")
        print("")
        for i in lista_compra:
            print(f"{i}   {lista_compra[i]}")
            total+=lista_compra[i]
        print(f"Total   {total}")

if __name__ == '__main__':
    main()