import math
import random
numSecreto = math.ceil(random.random() * 100)

while True:
    num = int(input("Digite um número: "))
    if num == numSecreto:
        print("Você acertou!")
        break
    elif num < numSecreto:
        print("O número secreto é maior")
    else:
        print("O número secreto é menor")
