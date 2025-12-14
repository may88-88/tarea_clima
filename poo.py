# Programación Orientada a Objetos
# Cálculo del promedio semanal del clima

class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio


def main():
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print("El promedio semanal es:", promedio)

main()
