from src.ejercicios.funciones import usuario, contrasenia_por_defecto

nombre = input("Ingrese su nombre: ")
username = usuario(nombre)

while 'juan' not in username and 'maria' not in username:
    dni = int(input("Ingrese su DNI: "))
    password = contrasenia_por_defecto(dni)
    print("El usuario para ingresar al sistema es:", username)
    print("La contraseña por defecto es:", password)
    nombre = input("Ingrese su nombre: ")
    username = usuario(nombre)