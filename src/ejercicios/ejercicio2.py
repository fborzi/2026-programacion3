from src.ejercicios.funciones import es_par

numero = int(input("Ingrese un número entero: "))

if es_par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")