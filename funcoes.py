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

def verifica_ganhador(jogadores):
    for num_jogador, pecas in jogadores.items():
        if len(pecas) == 0:
            return num_jogador
    return -1

def conta_pontos(pecas):
    total = 0
    for peca in pecas:
        total += peca[0] + peca[1]
    return total

def posicoes_possiveis(mesa, pecas):
    if len(mesa) == 0:
        return list(range(len(pecas)))
    ponta_esquerda = mesa[0][0]
    ponta_direita = mesa[-1][1]
    posicoes = []
    for i, peca in enumerate(pecas):
        if ponta_esquerda in peca or ponta_direita in peca:
            posicoes.append(i)
    return posicoes