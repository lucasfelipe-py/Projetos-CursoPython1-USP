def computador_escolhe_jogada(n, m):
    troca_turno = False
    iteracao = 1
    
    while troca_turno == False:
        if ((n - iteracao) % (m + 1)) == 0:
            escolha_computador = iteracao
            troca_turno = True
            return escolha_computador
        if iteracao >= m:
            escolha_computador = m
            troca_turno = True
            return escolha_computador
        else:
            iteracao += 1
#-------------------------------------------------------------------
def usuario_escolhe_jogada(m):
    troca_turno = False
    
    while troca_turno == False:
        pcs_remover = int(input('Quantas peças você vai tirar? '))
        print()
        
        if pcs_remover >= 1 and pcs_remover <= m:
            escolha_usuario = pcs_remover
            troca_turno = True
            return escolha_usuario
        else:
            print('Oops! Jogada inválida! Tente de novo.\n')
#------------------------------------------------------------------
def partida():
    n_escolhido = int(input('Quantas peças? '))
    m_escolhido = int(input('Limite de peças por jogada? '))
    print()
    pcs_restantes = n_escolhido
    
    if ((n_escolhido) % (m_escolhido + 1)) == 0:
        print('Você começa!')
        bot_jogou = True
    else:
        print('Computador começa!')
        bot_jogou = False
  
    while pcs_restantes > 0:
        if bot_jogou == True:
            jogada = usuario_escolhe_jogada(m_escolhido)
            print(f'Você tirou {jogada} peça(s)')
            pcs_restantes -= jogada
            if pcs_restantes > 1:
                print(f'Agora restam {pcs_restantes} peças no tabuleiro.')
            else:
                print(f'Agora resta apenas uma peça no tabuleiro.')
            bot_jogou = False
        else:
            jogada = computador_escolhe_jogada(pcs_restantes, m_escolhido)
            print()
            print(f'O computador tirou {jogada} peça(s)')
            pcs_restantes -= jogada
            if pcs_restantes > 1:
                print(f'Agora restam {pcs_restantes} peças no tabuleiro.\n')
            else:
                print(f'Agora resta apenas uma peça no tabuleiro.\n')
            bot_jogou = True
    
    print('Fim do jogo! O computador ganhou!\n')
#------------------------------------------------------------------------
def campeonato():
    print('**** Rodada 1 *****\n')
    partida()
    print('**** Rodada 2 *****\n')
    partida()
    print('**** Rodada 3 *****\n')
    partida()
    print('**** Final do campeonato! *****\n')
    print('Placar: Você 0 X 3 Computador')
#-----------------------------------------------------------------------
def main():
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    
    camp_ou_isolada = int(input())
    
    if camp_ou_isolada == 1:
        print('Você escolheu uma partida isolada!\n')
        print('**** Rodada 1 *****\n')
        partida()
    elif camp_ou_isolada == 2:
        print('Você escolheu um campeonato!\n')
        campeonato()
#----------------------------------------------------------------------       
main()