import string

def verificar_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())

    return texto_limpo == texto_limpo[::-1]

def main():
    entrada = input("Digite uma palavra ou frase: ")

    if verificar_palindromo(entrada):
        print("A palavra ou frase é um palíndromo.")
    else:
        print("A palavra ou frase não é um palíndromo.")

    main()
