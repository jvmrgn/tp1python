print("Por favor responda os dados solicitados.")

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

print(f"Resultado soma: {soma(num1, num2)}\nResultado subtração: {sub(num1, num2)}\nResultado multiplicação: {mult(num1, num2)}\nResultado divisão: {div(num1, num2)}")