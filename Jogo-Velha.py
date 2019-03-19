winLetras = {'1': ['a', 'b', 'c'],
             '2': ['d', 'e', 'f'],
             '3': ['g', 'h', 'i'],
             '4': ['a', 'd', 'g'],
             '5': ['b', 'e', 'h'],
             '6': ['c', 'f', 'i'],
             '7': ['a', 'e', 'i'],
             '8': ['c', 'e', 'g']
             }
listaDic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}
vitoria = False
cont = 1
player = 'x'
continuar = True


def imprime():
    print("_1_|_2_|_3_")
    print("_4_|_5_|_6_")
    print(" 7 | 8 | 9 ")


def pos1(listadici):
    if listadici['a'] == 0:
        print("\n___|", end="")
    elif listadici['a'] == 1:
        print("\n_X_|", end="")
    elif listadici['a'] == 2:
        print("\n_O_|", end="")


def pos2(listadici):
    if listadici['b'] == 0:
        print("___|", end="")
    elif listadici['b'] == 1:
        print("_X_|", end="")
    elif listadici['b'] == 2:
        print("_O_|", end="")


def pos3(listadici):
    if listadici['c'] == 0:
        print("___")
    elif listadici['c'] == 1:
        print("_X_")
    elif listadici['c'] == 2:
        print("_O_")


def pos4(listadici):
    if listadici['d'] == 0:
        print("___|", end="")
    elif listadici['d'] == 1:
        print("_X_|", end="")
    elif listadici['d'] == 2:
        print("_O_|", end="")


def pos5(listadici):
    if listadici['e'] == 0:
        print("___|", end="")
    elif listadici['e'] == 1:
        print("_X_|", end="")
    elif listadici['e'] == 2:
        print("_O_|", end="")


def pos6(listadici):
    if listadici['f'] == 0:
        print("___")
    elif listadici['f'] == 1:
        print("_X_")
    elif listadici['f'] == 2:
        print("_O_")


def pos7(listadici):
    if listadici['g'] == 0:
        print("   |", end="")
    elif listadici['g'] == 1:
        print(" X |", end="")
    elif listadici['g'] == 2:
        print(" O |", end="")


def pos8(listadici):
    if listadici['h'] == 0:
        print("   |", end="")
    elif listadici['h'] == 1:
        print(" X |", end="")
    elif listadici['h'] == 2:
        print(" O |", end="")


def pos9(listadici):
    if listadici['i'] == 0:
        print("   ")
    elif listadici['i'] == 1:
        print(" X ")
    elif listadici['i'] == 2:
        print(" O ")


def imprimetabuleiros(lista):
    pos1(lista)
    pos2(lista)
    pos3(lista)
    pos4(lista)
    pos5(lista)
    pos6(lista)
    pos7(lista)
    pos8(lista)
    pos9(lista)


def winner(letras):
    for vallue in letras.values():
        x = 0
        o = 0
        for chave, valor in listaDic.items():
            if chave in vallue:
                if valor == 1:
                    x += 1
                if valor == 2:
                    o += 1
            if x == 3 or o == 3:
                print("Temos um campeão")
                return True


def incremento(posicao, vezjogador):
    if vezjogador == 'x':
        if posicao == 1:
            listaDic['a'] = 1
        elif posicao == 2:
            listaDic['b'] = 1
        elif posicao == 3:
            listaDic['c'] = 1
        elif posicao == 4:
            listaDic['d'] = 1
        elif posicao == 5:
            listaDic['e'] = 1
        elif posicao == 6:
            listaDic['f'] = 1
        elif posicao == 7:
            listaDic['g'] = 1
        elif posicao == 8:
            listaDic['h'] = 1
        elif posicao == 9:
            listaDic['i'] = 1
    if vezjogador == 'o':
        if posicao == 1:
            listaDic['a'] = 2
        elif posicao == 2:
            listaDic['b'] = 2
        elif posicao == 3:
            listaDic['c'] = 2
        elif posicao == 4:
            listaDic['d'] = 2
        elif posicao == 5:
            listaDic['e'] = 2
        elif posicao == 6:
            listaDic['f'] = 2
        elif posicao == 7:
            listaDic['g'] = 2
        elif posicao == 8:
            listaDic['h'] = 2
        elif posicao == 9:
            listaDic['i'] = 2
    return listaDic


def jogador(player1):
    if player1 == 'x':
        print("\nVez do jogador X")
        posx = int(input("Digite a posição do X (1 a 9)"))
        listadici = incremento(posx, 'x')
        imprimetabuleiros(listadici)
        return 'o'
    elif player1 == 'o':
        print("\nVez do jogador O")
        posx = int(input("Digite a posição do O (1 a 9)"))
        listadici = incremento(posx, 'o')
        imprimetabuleiros(listadici)
        return 'x'


while continuar:
    imprime()
    while not vitoria:
        player = jogador(player)
        cont += 1
        vitoria = winner(winLetras)
        if vitoria:
            if player == 'x':
                player = 'O'
            elif player == 'o':
                player = 'X'
            print("O JOGADOR %s GANHOU" % player)
            contin = input("\nContinuar? (S/N): ")
            if contin == 's' or contin == 'S':
                continuar = True
                vitoria = False
                player = 'x'
                listaDic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}
                cont = 1
            else:
                continuar = False
            break
        if cont > 9 and not vitoria:
            vitoria = True
            print("VELHA")
