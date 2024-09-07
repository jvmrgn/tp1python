
def inicio():
  print("Você está em uma floresta escura.")
  print("Você pode ir para a esquerda ou para a direita.")
  escolha = input("Digite 'esquerda' ou 'direita': ").lower()

  if escolha == 'esquerda':
      encontro_urso()
  elif escolha == 'direita':
      encontro_cabana()
  else:
      print("Escolha inválida. Tente novamente.")
      inicio()

def encontro_urso():
  print("\nVocê encontra um urso!")
  print("Você pode lutar ou correr.")
  escolha = input("Digite 'lutar' ou 'correr': ").lower()

  if escolha == 'lutar':
      print("\nVocê tenta lutar com o urso, mas ele é muito forte. Você perdeu.")
  elif escolha == 'correr':
      print("\nVocê corre e consegue escapar do urso. Você está seguro, por enquanto.")
      encontro_cabana()
  else:
      print("Escolha inválida. Tente novamente.")
      encontro_urso()

def encontro_cabana():
  print("\nVocê encontra uma cabana abandonada.")
  print("Você pode entrar ou continuar andando.")
  escolha = input("Digite 'entrar' ou 'continuar': ").lower()

  if escolha == 'entrar':
      print("\nDentro da cabana, você encontra comida e água. Você sobreviveu!")
  elif escolha == 'continuar':
      print("\nVocê continua andando, mas acaba se perdendo na floresta. Você perdeu.")
  else:
      print("Escolha inválida. Tente novamente.")
      encontro_cabana()

def main():
  print("Bem-vindo à aventura na floresta!")
  inicio()

main()