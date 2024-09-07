def votar():
  votos_opcao1 = 0
  votos_opcao2 = 0
  votos_opcao3 = 0

  while True:
      print("Escolha uma opção para votar:")
      print("1. Opção 1")
      print("2. Opção 2")
      print("3. Opção 3")
      print("4. Encerrar votação")

      try:
          voto = int(input("Digite o número da opção escolhida: "))
          if voto == 1:
              votos_opcao1 += 1
              print("Você votou na Opção 1.")
          elif voto == 2:
              votos_opcao2 += 1
              print("Você votou na Opção 2.")
          elif voto == 3:
              votos_opcao3 += 1
              print("Você votou na Opção 3.")
          elif voto == 4:
              print("Votação encerrada.")
              break
          else:
              print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

      except ValueError:
          print("Entrada inválida. Por favor, digite um número.")

  print("\nResultados da votação:")
  print(f"Opção 1: {votos_opcao1} votos")
  print(f"Opção 2: {votos_opcao2} votos")
  print(f"Opção 3: {votos_opcao3} votos")

  votar()