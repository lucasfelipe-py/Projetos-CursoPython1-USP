def computador_escolhe_jogada(n, m):
    troca_turno = False
    x = 1
    while troca_turno == False:
        if ((n - x) % (m + 1)) == 0:
            escolha_computador = x
            troca_turno = True
            return escolha_computador
        if x >= m:
            escolha_computador = m
            troca_turno = True
            return escolha_computador
        else:
            x += 1
#-------------------------------------------------------------------
def usuario_escolhe_jogada(n, m):
    troca_turno = False
    
    while troca_turno == False:
        pcs_remover = int(input('Quantas peças você vai tirar? '))
        print()
        
        if (pcs_remover >= 1) and (pcs_remover <= m):
            escolha_usuario = pcs_remover
            troca_turno = True
            return escolha_usuario
        else:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
#------------------------------------------------------------------
def partida():
    n_esc = int(input('Quantas peças? '))
    m_esc = int(input('Limite de peças por jogada? '))
    print()
    pcs_restantes = n_esc
    
    if ((n_esc) % (m_esc + 1)) == 0:
        print('Você começa!')
        bot_jogou = True
    else:
        print('Computador começa!')
        bot_jogou = False
  
    while pcs_restantes > 0:
        if bot_jogou == True:
            jogada = usuario_escolhe_jogada(pcs_restantes, m_esc)
            print(f'Você tirou {jogada} peça(s)')
            pcs_restantes = pcs_restantes - jogada
            if pcs_restantes > 1:
                print(f'Agora restam {pcs_restantes} peças no tabuleiro.')
            if pcs_restantes == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')
            bot_jogou = False
        else:
            jogada = computador_escolhe_jogada(pcs_restantes, m_esc)
            print()
            print(f'O computador tirou {jogada} peça(s)')
            pcs_restantes = pcs_restantes - jogada
            if pcs_restantes > 1:
                print(f'Agora restam {pcs_restantes} peças no tabuleiro.')
                print()
            if pcs_restantes == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')
                print()
            bot_jogou = True
    
    if pcs_restantes == 0:
        if bot_jogou == True:
            print('Fim do jogo! O computador ganhou!')
        else: 
            print('Fim do jogo! Você ganhou!')
#------------------------------------------------------------------------
def campeonato():
    print()
    print('**** Rodada 1 *****')
    print()
    partida()
    print()
    print('**** Rodada 2 *****')
    print()
    partida()
    print()
    print('**** Rodada 3 *****')
    print()
    partida()
    print()
    print('**** Final do campeonato! *****')
    print()
    print('Placar: Você 0 X 3 Computador')
#-----------------------------------------------------------------------
def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    
    c_ou_p = int(input())
    
    if c_ou_p == 1:
        print('Você escolheu uma partida isolada!')
        print()
        print('**** Rodada 1 *****')
        print()
        partida()
    if c_ou_p == 2:
        print('Você escolheu um campeonato!')
        campeonato()
#----------------------------------------------------------------------       
main()