# Programación Tradicional
# Cálculo del promedio semanal del clima

def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print("El promedio semanal es:", promedio)

main()