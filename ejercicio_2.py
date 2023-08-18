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

mensaje = """
¿Que conversión desea realizar?
1) centímetros -> pulgadas
2) metros -> kilometros
3) onzas -> gramos
4) millas -> kilometros
5) celcius -> fahrenheit
6) Salir
"""
opcion = int(input(mensaje))

while(opcion != 6):
    medida_1 = float(input("Ingrese la primera medida a convertir"))
    medida_2 = float(input("Ingrese la segunda medida a convertir"))