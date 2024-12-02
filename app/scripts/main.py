from app.scripts.charfun import es_palindromo

def main():
    frase = ""
    while frase.lower() != 'salir':
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ") 

        # Comprobar si es palíndromo 
        if es_palindromo(frase): 
            print("La frase es palíndroma.") 
        else: 
           print("La frase no es palíndroma.")
    else:
        print("Programa finalizado.")