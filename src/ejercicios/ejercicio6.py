from src.ejercicios.funciones import suma_digitos, es_par

numero = int(input("Ingrese un número entero: "))
cantidad_impares = 0

while 10 <= suma_digitos(numero) <= 50:
    if not es_par(numero):
        cantidad_impares += 1

print("La cantidad de números impares ingresados es:", cantidad_impares)