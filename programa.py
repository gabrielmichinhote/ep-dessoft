import funcoes

RESET = '\033[0m'
VERMELHO = '\033[91m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CIANO = '\033[96m'
BRANCO = '\033[97m'
NEGRITO = '\033[1m'

def desenha_peca(peca):
    cores = [BRANCO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO]
    v1, v2 = peca[0], peca[1]
    cor1 = cores[v1 % len(cores)]
    cor2 = cores[v2 % len(cores)]
    return f"{cor1}[{v1}|{cor2}{v2}]{RESET}"

def mostra_mesa(mesa):
    if len(mesa) == 0:
        print(f"\n{AMARELO}╔════════════════════════════════════╗{RESET}")
        print(f"{AMARELO}║          MESA VAZIA                ║{RESET}")
        print(f"{AMARELO}╚════════════════════════════════════╝{RESET}")
    else:
        print(f"\n{AMARELO}╔════════════════════════════════════╗{RESET}")
        print(f"{AMARELO}║ MESA:{RESET}", end=" ")
        for peca in mesa:
            print(desenha_peca(peca), end=" ")
        print(f"{AMARELO}║{RESET}")
        print(f"{AMARELO}╚════════════════════════════════════╝{RESET}")

def mostra_pecas(pecas, posicoes):
    print(f"\n{CIANO}Suas peças:{RESET}")
    for i, peca in enumerate(pecas):
        if i in posicoes:
            print(f"  {VERDE}{NEGRITO}[{i}]{RESET} {desenha_peca(peca)} {VERDE}← PODE JOGAR{RESET}")
        else:
            print(f"  [{i}] {desenha_peca(peca)}")

def valida_input_numero(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print("numero invalido")
        except ValueError:
            print("Digite um numero valido!")

def jogar_partida():
    num_jogadores = valida_input_numero("Quantos jogadores? (2-4): ", 2, 4)
    pecas = funcoes.cria_pecas()
    jogo = funcoes.inicia_jogo(num_jogadores, pecas)
    jogador_atual = 0

    while True:
        print(f"\n{'='*50}")
        print(f"{NEGRITO}TURNO DO JOGADOR {jogador_atual}{RESET}")
        print('='*50)
        mostra_mesa(jogo['mesa'])
        print(f"\n{CIANO}Situação dos jogadores:{RESET}")

        for j in jogo['jogadores']:
            num_pecas = len(jogo['jogadores'][j])
            if j == jogador_atual:
                print(f"  {VERDE}► Jogador {j}: {num_pecas} peça(s) {RESET}")
            else:
                print(f"    Jogador {j}: {num_pecas} peça(s)")
        print(f"  Monte: {len(jogo['monte'])} peça(s)")
        ganhador = funcoes.verifica_ganhador(jogo['jogadores'])

        if ganhador != -1:
            print(f"\n{AMARELO}{'='*50}{RESET}")

            if ganhador == 0:
                print(f"{VERDE}{NEGRITO}★★★ PARABÉNS! VOCÊ VENCEU! ★★★{RESET}")
            else:
                print(f"{VERMELHO}VOCÊ PERDEU! Jogador {ganhador} venceu!{RESET}")
            print(f"{AMARELO}{'='*50}{RESET}")
            print(f"\n{CIANO}Pontos finais:{RESET}")

            for j in jogo['jogadores']:
                pontos = funcoes.conta_pontos(jogo['jogadores'][j])
                print(f"  Jogador {j}: {pontos} pontos")
            return

        minhas_pecas = jogo['jogadores'][jogador_atual]
        posicoes = funcoes.posicoes_possiveis(jogo['mesa'], minhas_pecas)
        
        if len(posicoes) == 0:
            print(f"\n{VERMELHO}Não tem peças possíveis. PEGANDO DO MONTE{RESET}")

            if len(jogo['monte']) > 0:
                peca_monte = jogo['monte'].pop(0)
                minhas_pecas.append(peca_monte)
                print(f"Pegou: {desenha_peca(peca_monte)}")
            else:
                print(f"{AMARELO}Monte vazio! Passando a vez...{RESET}")

        else:
            mostra_pecas(minhas_pecas, posicoes)
            while True:
                try:
                    escolha = int(input(f"\n{VERDE}Escolha a peça {posicoes}: {RESET}"))
                    if escolha in posicoes:
                        peca = minhas_pecas.pop(escolha)
                        jogo['mesa'] = funcoes.adiciona_na_mesa(peca, jogo['mesa'])
                        print(f"{VERDE}✓ Peça {desenha_peca(peca)} jogada com sucesso!{RESET}")
                        break
                    else:
                        print(f"{VERMELHO}posicao invalida{RESET}")
                except ValueError:
                    print(f"{VERMELHO}Digite um numero valido!{RESET}")
        jogador_atual = (jogador_atual + 1) % num_jogadores
        input(f"\n{CIANO}[Pressione ENTER para continuar]{RESET}")

while True:
    print(f"\n{AMARELO}{'='*50}")
    print(f"{NEGRITO}         🎲 JOGO DE DOMINÓ 🎲{RESET}")
    print(f"{AMARELO}{'='*50}{RESET}\n")
    jogar_partida()
    print(f"\n{CIANO}Deseja jogar novamente?{RESET}")
    resposta = input("Digite 's' para sim ou 'n' para não: ").lower()
    if resposta != 's':
        print(f"\n{VERDE}Obrigado por jogar! Até a próxima! 👋{RESET}\n")
        break