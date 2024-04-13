def computador_escolhe_jogada(n, m):
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return min(n, m)

def usuario_escolhe_jogada(m):
   while True:
        try:
            jogada = int(input('Quantas peças você vai tirar? '))
            if 1 <= jogada <= m:
                return jogada
            else:
                print(f'Oops! Jogada inválida! Tente de novo. Você deve tirar entre 1 e {m} peças.\n')
        except ValueError:
            print("Por favor, digite um número.\n")

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    
    vez_do_computador = (n % (m + 1)) != 0
    if vez_do_computador:
        print('Computador começa!')
    else:
        print('Você começa!')

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f'\nO computador tirou {jogada} peça(s).')
            vez_do_computador = False
        else:
            jogada = usuario_escolhe_jogada(m)
            n -= jogada
            print(f'\nVocê tirou {jogada} peça(s).')
            vez_do_computador = True
        
        if n > 1:
            print(f'Agora restam {n} peças no tabuleiro.\n')
        elif n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
    
    print('Fim do jogo! O computador ganhou!\n')

def campeonato():
    for i in range(1, 4):
        print(f'**** Rodada {i} *****\n')
        partida()
    
    print('**** Final do campeonato! *****\n')
    print('Placar: Você 0 X 3 Computador')

def main():
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    escolha = int(input())

    if escolha == 1:
        partida()
    elif escolha == 2:
        campeonato()

if __name__ == '__main__':
    main()
