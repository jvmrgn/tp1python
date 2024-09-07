print("Qual operação você quer fazer?")
print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

typeAccount = input("Digite o número da operação: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b): 
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

if typeAccount == "1":
    print(f"Resultado: {soma(num1, num2)}")
elif typeAccount == "2":
    print(f"Resultado: {sub(num1, num2)}")
elif typeAccount == "3":
    print(f"Resultado: {mult(num1, num2)}")
elif typeAccount == "4":
    print(f"Resultado: {div(num1, num2)}")
else:
    print("Operação inválida")




