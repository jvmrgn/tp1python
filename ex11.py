import random

def lancar_dado(num_dados):
    resultados = [random.randint(1, 6) for _ in range(num_dados)]
    return resultados

def main():
    try:
        num_dados = int(input("Quantos dados você deseja lançar? "))
        
        if num_dados <= 0:
            print("O número de dados deve ser um número positivo.")
            return
        
        resultados = lancar_dado(num_dados)
        
        print(f"Resultados dos lançamentos dos {num_dados} dados:")
        for i, resultado in enumerate(resultados, start=1):
            print(f"Dado {i}: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
