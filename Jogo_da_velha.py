a = [" "," "," "]
b = [" "," "," "]
c = [" "," "," "]
venceu = 0
jogadas = 0
print("         Esse é o jogo da velha\n"
      "O Jogador1 usará X e o Jogador2 usará O:\n"
      "Na sequencia de 1 a 9, escolha onde deseja posicionar suas jogadas!")
print()
while venceu != "x" and venceu != "o":
    jogador1 = 0
    while jogador1 == 0:
        while jogador1 <1 or jogador1>9:
            print(a), print(b), print(c)
            print("Digite um número válido de 1 a 9:")
            jogador1 = int(input("Jogador1 Digite um numero: "))
            if jogador1 == 1:
                if a[0] != "x" and a[0] != "o":
                    a[0] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 2:
                if a[1] != "x" and a[1] != "o":
                    a[1] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 3:
                if a[2] != "x" and a[2] != "o":
                    a[2] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 4:
                if b[0] != "x" and b[0] != "o":
                    b[0] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 5:
                if b[1] != "x" and b[1] != "o":
                    b[1] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 6:
                if b[2] != "x" and b[2] != "o":
                    b[2] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 7:
                if c[0] != "x" and c[0] != "o":
                    c[0] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 8:
                if c[1] != "x" and c[1] != "o":
                    c[1] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
            elif jogador1 == 9:
                if c[2] != "x" and c[2] != "o":
                    c[2] = "x"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador1 = 0
    print()
    jogadas = jogadas + 1
    if jogadas == 9:
        print("      Essa partida deu EMPATE!")
        break
    print(f"A quantidade de jogadas atualmente é:{jogadas}\n")
    jogador2 = 0
    while jogador2 == 0:
        while jogador2 <1 or jogador2 > 9:
            print(a), print(b), print(c)
            print("Digite um número válido de 1 a 9:")
            jogador2 = int(input("Jogador2 Digite um numero: "))
            if jogador2 == 1:
                if a[0] != "x" and a[0] != "o":
                    a[0] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 2:
                if a[1] != "x" and a[1] != "o":
                    a[1] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 3:
                if a[2] != "x" and a[2] != "o":
                    a[2] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 4:
                if b[0] != "x" and b[0] != "o":
                    b[0] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 5:
                if b[1] != "x" and b[1] != "o":
                    b[1] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 6:
                if b[2] != "x" and b[2] != "o":
                    b[2] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 7:
                if c[0] != "x" and c[0] != "o":
                    c[0] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 8:
                if c[1] != "x" and c[1] != "o":
                    c[1] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
            elif jogador2 == 9:
                if c[2] != "x" and c[2] != "o":
                    c[2] = "o"
                else:
                    print("Esse número já foi digitado! Tente novamente!")
                    jogador2 = 0
    print()
    jogadas = jogadas +1
    if jogadas == 9:
        print("      Essa partida deu EMPATE!")
        break
    print(f"A quantidade de jogadas atualmente é:{jogadas}")
    if a[0] == a[1] == a[2]:
        if a[0] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")

        elif a[0] =="o":
            print(f"O jogador Jogador2 venceu!")
            break
    elif b[0] == b[1] == b[2]:
        if b[0] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif b[0] == "o":
            venceu = "o"
            print(f"O jogador Jogador2 venceu!")
            break
    elif c[0] == c[1] == c[2]:
        if c[0] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif c[0] == "o":
            venceu = "o"
            print(f"O jogador jogador2 venceu!")
            break
    elif a[0] == b[0] == c[0]:
        if b[0] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif a[0] == "o":
            venceu = "o"
            print(f"O jogador jogador2 venceu!")
            break
    elif a[1] == b[1] == c[1]:
        if a[1] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif a[1] == "o":
            venceu = "o"
            print(f"O jogador jogador2 venceu!")
            break
    elif a[2] == b[2] == c[2]:
        if a[2] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif a[2] == "o":
            venceu = "o"
            print(f"O jogador jogador2 venceu!")
            break
    elif a[0] == b[1] == c[2]:
        if a[0] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif a[0] == "o":
            venceu = "o"
            print(f"O jogador jogador2 venceu!")
            break
    elif a[2] == b[1] == c[0]:
        if a[2] == "x":
            venceu = "x"
            print(f"O jogador Jogador1 venceu!")
            break
        elif a[2] == "o":
            venceu = "o"
            print(f"O jogador jogador2 venceu!")
            break
    if venceu == "x" or venceu == "o":
        print("A partida acabou!")
        break