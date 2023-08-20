# Cree un programa conversor de unidades, donde muestre una serie de unidades a convertir y la
# opción de terminar el programa. Si se selecciona la opción de terminar el programa, se debe
# terminar la ejecución del mismo. Por ejemplo:
# a. ¿Que conversión desea realizar?
# b. 1) centímetros -> pulgadas
# c. 2) metros -> kilometros
# d. 3) onzas -> gramos
# e. 4) millas -> kilometros
# f. 5) celcius -> fahrenheit
# g. 6) Salir

def main():
    mensaje = """
    ¿Que conversión desea realizar?
    1) centímetros -> pulgadas
    2) metros -> kilometros
    3) onzas -> gramos
    4) millas -> kilometros
    5) celcius -> fahrenheit
    6) Salir

Opcion: """

    opcion = int(input(mensaje))

    while(opcion != 6):
        medida = float(input("Ingrese la medida a convertir: "))
        if opcion == 1:
            print("centímetros -> pulgadas")
            pulgadas = medida / 2.54
            print(f"{medida}cm son {pulgadas}in")
            print("")
        elif opcion == 2:
            print("metros -> kilometros")
            kilometros = medida / 1000
            print(f"{medida}m son {kilometros}km")
            print("")
        elif opcion == 3:
            print("onzas -> gramos")
            gramos = medida * 28.35
            print(f"{medida}oz son {gramos}g")
            print("")
        elif opcion == 4:
            print("millas -> kilometros")
            kilometros = medida * 1.609
            print(f"{medida}mi son {kilometros}km")
            print("")
        elif opcion == 5:
            print("celcius -> fahrenheit")
            fahrenheit = (medida * 9/5) + 32
            print(f"{medida}°C son {fahrenheit}°F")
            print("")
        else:
            print("Opcion no valida")
            print("")
        opcion = int(input("Opcion: "))
    print("Programa terminado")
        

if __name__ == '__main__':
    main()