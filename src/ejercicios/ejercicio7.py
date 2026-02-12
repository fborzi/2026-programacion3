from src.ejercicios.funciones import maximo

mayor = 0

for i in range(5):
    numero = abs(int(input(f"Ingrese el numero {i+1}: ")))
    anterior = numero
    mayor = maximo(anterior, numero)

print("El numero mayor es:", mayor)
