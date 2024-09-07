import random

def lancar_dados(quantidade):
    resultados = []
    for _ in range(quantidade):
        resultado = random.randint(1, 6) 
        resultados.append(resultado)
    return resultados

quantidade = int(input("Quantos dados você quer lançar? "))
if quantidade > 0: 
    resultados = lancar_dados(quantidade)
    print(f"Você lançou {quantidade} dado(s) e obteve os seguintes resultados: {resultados}")
else: 
    print("A quantidade de dados deve ser maior ou igual a 1.")
