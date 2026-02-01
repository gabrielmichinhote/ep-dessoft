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


def adiciona_na_mesa(peca, mesa):
    if len(mesa) == 0:
        return [peca]
    ponta_esquerda = mesa[0][0]
    ponta_direita = mesa[-1][1]
    if peca[0] == ponta_esquerda or peca[1] == ponta_esquerda:
        if peca[1] == ponta_esquerda:
            mesa.insert(0, peca)
        else:
            mesa.insert(0, [peca[1], peca[0]])
    elif peca[0] == ponta_direita or peca[1] == ponta_direita:
        if peca[0] == ponta_direita:
            mesa.append(peca)
        else:
            mesa.append([peca[1], peca[0]])
    return mesa