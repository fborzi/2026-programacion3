from src.ejercicios.funciones import usuario, contrasenia_por_defecto

nombre = input("Ingrese su nombre: ")

while 'juan' not in usuario(nombre) and 'maria' not in usuario(nombre):
    usuario = usuario(nombre)
    dni = int(input("Ingrese su DNI: "))
    password = contrasenia_por_defecto(dni)
    print("El usuario para ingresar al sistema es:", usuario)
    print("La contraseña por defecto es:", password)
    nombre = input("Ingrese su nombre: ")