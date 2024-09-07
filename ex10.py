import random

def criar_historia():
    personagens = ["um dragão", "uma princesa", "um cavaleiro", "um mago", "um robô", "um pirata"]
    acoes = ["encontrou", "lutou contra", "fugiu de", "fez amizade com", "descobriu", "transformou-se em"]
    locais = ["em um castelo", "em uma floresta encantada", "em uma ilha deserta", "no espaço sideral", "em uma caverna secreta", "em uma cidade futurista"]

    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)

    historia = f"Era uma vez {personagem} que {acao} {local}."
    return historia

print(criar_historia())