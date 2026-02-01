import random

def cria_pecas():
    pecas = []
    for i in range(7):
        for j in range(i, 7):
            pecas.append([i, j])
    random.shuffle(pecas)
    return pecas


def inicia_jogo(num_jogadores, pecas):
    jogo = {
        'jogadores': {},
        'monte': [],
        'mesa': []
    }
    pecas_por_jogador = 7
    for i in range(num_jogadores):
        inicio = i * pecas_por_jogador
        fim = inicio + pecas_por_jogador
        jogo['jogadores'][i] = pecas[inicio:fim]
    total_distribuidas = num_jogadores * pecas_por_jogador
    jogo['monte'] = pecas[total_distribuidas:]
    return jogo