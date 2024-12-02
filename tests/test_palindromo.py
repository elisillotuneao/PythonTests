import unittest
from app.scripts.charfun import es_palindromo 


class TestEsPalindromo(unittest.TestCase):

    def test_cadena_pal(self):
        cadenas_pal = ["ana","elle","iiiiii"]  # Lista de cadenas palíndromas
        for i in cadenas_pal:
            resultado = es_palindromo(i)
            self.assertTrue(
                resultado,
                f"La cadena {i} debería ser un palíndromo, pero la función devolvió {resultado}."
            )
    
    def test_cadena_nopal(self):
        cadenas_nopal = ["hola","frase","cadena","nopal","fasasdas"]  # Lista de cadenas no palíndromas
        for i in cadenas_nopal:
            resultado = es_palindromo(i)
            self.assertFalse(
                resultado,
                f"La cadena {i} no debería ser un palíndromo, pero la función devolvió {resultado}."
            )

    def test_excepciones_tipo_incorrecto(self):
        entradas_invalidas = [20, [1, 2, 3], {"clave": "valor"}, None]
        for i in entradas_invalidas:
            with self.assertRaises(TypeError, msg=f"Se esperaba TypeError con la entrada {i}"):
                es_palindromo(i)

    def test_mayus(self):
        self.assertEqual('foo'.upper(), 'FOO') # Igualación entre mayúsculas y minúsculas

if __name__ == "__main__":
    unittest.main()