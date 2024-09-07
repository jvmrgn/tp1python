def classificar_palavras(palavras):
  curtas = []
  longas = []

  for palavra in palavras:
      if len(palavra) < 5:
          curtas.append(palavra)
      else:
          longas.append(palavra)

  return curtas, longas

def main():
  entrada = input("Digite as palavras separadas por espaço: ")
  palavras = entrada.split()

  if not palavras:
      print("Nenhuma palavra foi inserida.")
      return

  curtas, longas = classificar_palavras(palavras)

  print("\nPalavras curtas (menos de 5 letras):")
  for palavra in curtas:
      print(f"- {palavra}")

  print("\nPalavras longas (5 letras ou mais):")
  for palavra in longas:
      print(f"- {palavra}")

main()
