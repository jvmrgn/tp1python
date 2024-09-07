print("Por favor forneça um número de minutos para ser convertido em horas e minutos.")
minutos_totais = int(input("Digite o número de minutos: "))

def minutos_para_horas_e_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

def horas_e_minutos_para_minutos(horas, minutos):
    return horas * 60 + minutos

horas, minutos = minutos_para_horas_e_minutos(minutos_totais)
print(f"{minutos_totais} minutos correspondem a {horas} horas e {minutos} minutos.")

minutos_de_volta = horas_e_minutos_para_minutos(horas, minutos)
print(f"{horas} horas e {minutos} minutos correspondem a {minutos_de_volta} minutos totais.")
