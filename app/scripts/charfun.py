"""
charfun.py 
Programa que determina si una cadena proporcionada por el usuario es palíndroma. 
Para ello se preguntará por teclado al usuario tantas veces como quiera hasta que escriba la palabra salir. 

Ultima Modificación. 21/11/2024 
Autor. Gregorio Coronado Morón 
Dependencias. Unicodedata 
""" 

import unicodedata 

def es_palindromo(cadena): 
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes. Controla el tipo de datos que se introducen.
    """

    if not isinstance(cadena, str):
        raise TypeError(f"Debe introducirse una cadena de texto, pero se recibió {type(cadena).__name__}")
    
    # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos 
    cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum()) 

    # Comparar la cadena limpia con su reverso 
    return cadena_limpia == cadena_limpia[::-1]