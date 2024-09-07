def combinar_nomes(nome1, nome2):
    metade_nome1 = nome1[:len(nome1)//2]
    metade_nome2 = nome2[len(nome2)//2:]

    nome_combinado = metade_nome1 + metade_nome2

    return nome_combinado

nome1 = input("Primeiro nome: ")
nome2 = input("Segundo nome: ")

nome_combinado = combinar_nomes(nome1, nome2)
print(f"Nomes combinados: {nome_combinado}")
