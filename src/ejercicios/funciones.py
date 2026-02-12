def es_par(numero: int) -> bool:
    """Determina si un número es par o impar.

    Args:
        numero (int): El número a evaluar.

    Returns:
        bool: True si el número es par, False si es impar.
    """
    return numero % 2 == 0

def suma_digitos(numero: int) -> int:
    """Calcula la suma de los dígitos de un número.

    Args:
        numero (int): El número del cual se sumarán los dígitos.

    Returns:
        int: La suma de los dígitos del número.
    """
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

def mostrar_suma_digitos(numero: int) -> None:
    """Muestra la suma de los dígitos de un número.

    Args:
        numero (int): El número del cual se sumarán los dígitos.
    """
    suma = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {suma}")

def maximo(num1: int, num2: int) -> int:
    """Determina el número máximo entre dos números.

    Args:
        num1 (int): El primer número.
        num2 (int): El segundo número.

    Returns:
        int: El número máximo entre num1 y num2.
    """
    return abs(num1) if abs(num1) > abs(num2) else abs(num2)

def quitar_tildes(cadena: str) -> str:
    """Elimina las tildes de una cadena de texto.

    Args:
        cadena (str): La cadena de texto a procesar.

    Returns:
        str: La cadena de texto sin tildes.
    """
    tildes = "áéíóúÁÉÍÓÚ"
    sin_tildes = "aeiouAEIOU"
    trans = cadena.maketrans(tildes, sin_tildes)
    return cadena.translate(trans)

def usuario(nombre: str) -> str:
    """Formatear el nombre de usuario

    Args:
        nombre (str): Nombre y apellido de la persona.

    Returns:
        str: Usuario formateado.
    """
    nombres = nombre.lower().split(",")
    usuarios = (nombres[1].strip() +  nombres[0].strip()).split()
    usuario_formateado = ""
    for u in usuarios:
        usuario_formateado += u

    return quitar_tildes(usuario_formateado)

def contrasenia_por_defecto(dni: int) -> str:
    """Genera una contraseña por defecto a partir del DNI.

    Args:
        dni (int): El número de DNI de la persona.

    Returns:
        str: La contraseña generada a partir del DNI.
    """
    return str(dni)[-4:]

def titulo(cadena: str) -> str:
    """Devuelve un texto convertido a title().

    Returns:
        str: El titulo.
    """
    titulo_capitalizado = ""
    lista_palabras = cadena.split(" ")
    for palabra in lista_palabras:
        titulo_capitalizado += palabra.capitalize() + " "
    titulo_capitalizado = titulo_capitalizado.strip()

    return titulo_capitalizado