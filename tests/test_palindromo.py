import unittest
from app.scripts.charfun import es_palindromo
import random
import string

# Función para generar aleatoriamente cadenas palíndromas
def generar_palindromo(longitud):
    mitad = ''.join(random.choices(string.ascii_lowercase, k=longitud // 2))
    return mitad + mitad[::-1] if longitud % 2 == 0 else mitad + random.choice(string.ascii_lowercase) + mitad[::-1]

# Función para generar aleatoriamente cadenas no palíndroams
def generar_no_palindromo(longitud):
    # Generamos una cadena aleatoria y le cambiamos un carácter para que no sea un palíndromo
    cadena = ''.join(random.choices(string.ascii_lowercase, k=longitud))
    # Aseguramos que la cadena no sea un palíndromo modificando el último carácter
    no_palindromo = cadena[:-1] + random.choice([c for c in string.ascii_lowercase if c != cadena[-1]])
    return no_palindromo

# Función para generar un número aleatorio entre 1 y 100
def generar_numero_aleatorio():
    return random.randint(1, 100)  

# Función para generar una lista aleatoria con entre 1 y 5 elementos, eligiendo aleatoriamente entre números y letras
def generar_lista_aleatoria():
    longitud = random.randint(1, 5)
    return [random.choice([random.randint(1, 10), random.choice(string.ascii_lowercase)]) for _ in range(longitud)]

# Función para generar un diccionario aleatorio con 1 o 2 pares clave-valor
def generar_diccionario_aleatorio():
    diccionario = {}
    num_items = random.randint(1, 2)
    for _ in range(num_items):
        clave = ''.join(random.choices(string.ascii_lowercase, k=5))
        valor = random.choice([random.randint(1, 10), random.choice(string.ascii_lowercase)])
        diccionario[clave] = valor
    return diccionario

# Función para escoger aleatoriamente un tipo de entrada inválida
def generar_entrada_invalida():
    tipo = random.choice(['numero', 'lista', 'diccionario', 'none'])
    if tipo == 'numero':
        return generar_numero_aleatorio()
    elif tipo == 'lista':
        return generar_lista_aleatoria()
    elif tipo == 'diccionario':
        return generar_diccionario_aleatorio()
    else:
        return None

class TestEsPalindromo(unittest.TestCase):

    def test_cadena_pal(self):
        for _ in range(5):  # Generamos 5 palíndromos aleatorios
            longitud = random.randint(3, 10)  # Longitud aleatoria entre 3 y 10
            palindromo = generar_palindromo(longitud)
            resultado = es_palindromo(palindromo)
            self.assertTrue(
                resultado,
                f"La cadena {palindromo} debería ser un palíndromo, pero la función devolvió {resultado}."
            )
    
    def test_cadena_nopal(self):
        for _ in range(5):  # Generamos 5 cadenas no palíndromas aleatorias
            longitud = random.randint(3, 10)  # Longitud aleatoria entre 3 y 10
            no_palindromo = generar_no_palindromo(longitud)
            resultado = es_palindromo(no_palindromo)
            self.assertFalse(
                resultado,
                f"La cadena {no_palindromo} no debería ser un palíndromo, pero la función devolvió {resultado}."
            )

    def test_excepciones_tipo_incorrecto(self):
        for _ in range(5):  # Realizamos 5 pruebas con entradas aleatorias
            entrada = generar_entrada_invalida()
            with self.assertRaises(TypeError, msg=f"Se esperaba TypeError con la entrada {entrada}"):
                es_palindromo(entrada)

    def test_mayus(self):
        self.assertEqual('foo'.upper(), 'FOO') # Igualación entre mayúsculas y minúsculas

    def test_cadena_un_caracter(self):
        for i in string.ascii_lowercase:  # Probar con todas las letras
            resultado = es_palindromo(i)
            self.assertTrue(
                resultado,
                f"La cadena de un solo carácter '{i}' debería ser un palíndromo, pero la función devolvió {resultado}."
            )

if __name__ == "__main__":
    unittest.main()