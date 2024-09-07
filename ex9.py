def calcular_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 25
    elif valor_compra > 400:
        desconto = 20
    elif valor_compra > 300:
        desconto = 18
    elif valor_compra > 200:
        desconto = 15
    elif valor_compra > 100:
        desconto = 10
    else:
        desconto = 0
    
    valor_desconto = valor_compra * (desconto / 100)
    valor_final = valor_compra - valor_desconto
    
    return valor_final, desconto, valor_desconto

valor_compra = float(input("Digite o valor da compra: R$ "))
valor_final, desconto, valor_desconto = calcular_desconto(valor_compra)

print(f"Valor original da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto}% (R$ {valor_desconto:.2f})")
print(f"Valor final com desconto: R$ {valor_final:.2f}")
