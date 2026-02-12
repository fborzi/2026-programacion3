from src.ejercicios.funciones import es_par

numero = -1
contador_pares = 0
contador_positivos = 0

while contador_pares <= 7:
    if es_par(numero):
        contador_pares += 1
        if numero > 0:
            contador_positivos += 1
    numero = int(input("Ingrese un número entero: "))

print("La cantidad de numeros pares positivos es:", contador_positivos)