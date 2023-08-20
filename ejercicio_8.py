# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro
# usando la primera función.

def area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

def volumen_cilindro(radio, altura):
    volumen = area_circulo(radio) * altura
    return volumen

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    print(f"Área del circulo: {area_circulo(radio)}")
    print(f"Volumen del cilindro: {volumen_cilindro(radio, altura)}")

if __name__ == '__main__':
    main()