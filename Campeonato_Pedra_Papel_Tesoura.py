cont = 0
jogador1 = 0
jogador2 = 0
player1 = 0
player2 = 0
novojogo = 1
while novojogo == 1:
    print("Olá, esse é o jogo de pedra, papel ou tesoura, onde vocês jogarão 3 partidas.\n"
          "Você deve escolher 1 para Pedra, 2 para Papel ou 3 para Tesoura.\n")
    while cont != 3:
        while player1 != 1 and player1 != 2 and player1 != 3:
            player1 = int(input("Jogador1, escolha um número: "))
            if player1 == 1:
                print("O Jogador1 escolheu: Pedra")
            elif player1 == 2:
                print("O Jogador1 escolheu: Papel")
            elif player1 == 3:
                print("O Jogador1 escolheu: Tesoura")
            else:
                print("Erro, digite um número válido")
        while player2 != 1 and player2 != 2 and player2 != 3:
            player2 = int(input("Jogador1, escolha um número: "))
            if player2 == 1:
                print("O Jogador2 escolheu: Pedra")
            elif player2 == 2:
                print("O Jogador2 escolheu: Papel")
            elif player2 == 3:
                print("O Jogador2 escolheu: Tesoura")
            else:
                print("Erro, digite um número válido")
            print()
        if player2 == 1 or player2 == 2 or player2 == 3:
            cont = cont + 1
        if player1 == player2:
            print("EMPATE! nenhum jogador pontuou!")
            print()
        elif player1 == 1 and player2 == 3:
            jogador1 = jogador1 + 1
            print("O Jogador 1 venceu essa partida!")
            print()
        elif player1 == 2 and player2 == 1:
            jogador1 = jogador1 + 1
            print("O Jogador 1 venceu essa partida!")
            print()
        elif player1 == 3 and player2 == 2:
            jogador1 = jogador1 + 1
            print("O Jogador 1 venceu essa partida!")
            print()
        else:
            jogador2 = jogador2 + 1
            print("O Jogador2 venceu essa partida!")
            print()
        if cont == 1:
            print("Iniciando Segunda Partida")
        elif cont == 2:
            print("Iniciando Terceira e Última Partida")
        player1 = 0
        player2 = 0
        if cont == 3:
            if jogador1 == jogador2:
                print("Empatados, ninguem venceu o torneio!")
            elif jogador1>jogador2:
                print("Jogador1 venceu o torneio de 3 partidas")
            elif jogador1<jogador2:
                print("Jogador2 venceu o torneio de 3 partidas")
            print()
    novojogo = int(input("Deseja iniciar o campeonato novamente, digite 1 para reiniciar, ou 0 para sair?? "))
    if novojogo == 1:
        cont = 0
        jogador1 = 0
        jogador2 = 0