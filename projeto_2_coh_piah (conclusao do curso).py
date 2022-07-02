import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada 
    com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
        print()

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # Diferença entre as_a e as_b:
    fi_ab = []
    n = len(as_b)

    while n > 0:
        x = as_a[n - 1] - as_b[n - 1]
        fi_ab.append(x)
        n -= 1
    
    # Módulo da diferença:
    n2 = len(fi_ab)
    total = 0
    while n2 > 0:
        x2 = abs(fi_ab[n2 - 1])
        total += x2
        n2 -= 1
    
    # Grau de similaridade
    sab = total / 6

    return sab

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Gerar uma lista de sentenças a partir de um texto
    lista_sentencas = separa_sentencas(texto)

    # Para cada sentença (em lista_sentencas): gerar uma lista de frases
    lista_frases = []
    qtdade_sentencas_iteracao = len(lista_sentencas)
    qtdade_sentencas = len(lista_sentencas)

    while qtdade_sentencas_iteracao > 0:
        frases = separa_frases(lista_sentencas[qtdade_sentencas_iteracao - 1])
        lista_frases += frases
        qtdade_sentencas_iteracao -= 1

    # Para cada frase em (em lista_frases): gerar uma lista de palavras
    lista_palavras = []
    qtdade_frases_iteracao = len(lista_frases)
    qtdade_frases = len(lista_frases)

    while qtdade_frases_iteracao > 0:
        palavras = separa_palavras(lista_frases[qtdade_frases_iteracao - 1])
        lista_palavras += palavras
        qtdade_frases_iteracao -= 1

    # Contar o número total de palavras e o número total de caracteres
    n_palavras_iteracao = len(lista_palavras)
    n_palavras = len(lista_palavras)

    soma_carac = 0

    while n_palavras_iteracao > 0:
        n_letras = len(lista_palavras[n_palavras_iteracao - 1])
        soma_carac += n_letras
        n_palavras_iteracao -= 1
    # soma_carac = Número total de caracteres
    # n_palavras = Número total de polavras

    # Soma dos caracteres das frases
    fr = len(lista_frases)
    soma_carac_frases = 0
    while fr > 0:
        x = len(lista_frases[fr - 1])
        soma_carac_frases += x
        fr -= 1
    # soma_carac_frases = Número total de caracteres frases

    # Soma dos caracteres das sentencas
    sent = len(lista_sentencas)
    soma_carac_sentencas = 0
    while sent > 0:
        x = len(lista_sentencas[sent - 1])
        soma_carac_sentencas += x
        sent -= 1
    # soma_carac_sentencas = Número total de caracteres sentenças
    
    # Soma dos tamanhos das palavras (quantas letras no total) / nº total de palavras
    wal_a = soma_carac / n_palavras

    # Nº de palavras diferentes / nº total de palavras:
    ttr_a = n_palavras_diferentes(lista_palavras) / n_palavras

    # Nº de palavras únicas / nº total de palavras:
    hlr_a = n_palavras_unicas(lista_palavras) / n_palavras

    # Soma do nº total de caracteres das sentenças / Nº total de sentenças
    sal_a = soma_carac_sentencas / qtdade_sentencas

    # Nº total de frases / nº de sentenças
    sac_a = qtdade_frases / qtdade_sentencas

    # Soma do número de caracteres em cada frase / nº total de frases
    pal_a = soma_carac_frases / qtdade_frases

    return [wal_a, ttr_a, hlr_a, sal_a, sac_a, pal_a]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) 
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    # Calcula as assinaturas dos textos (calcula_assinatura)
    n = len(textos) - 1
    i = 0
    assinaturas = []
    while n >= i:
        ass_calculada = calcula_assinatura(textos[i])
        assinaturas.append(ass_calculada)
        i += 1

    # Compara as assinaturas com a ass plagiada (compara_assinatura)
    n2 = len(assinaturas) - 1
    i = 0
    sab_textos = []
    while n2 >= i:
        ass_comparada = compara_assinatura(assinaturas[i], ass_cp)
        sab_textos.append(ass_comparada)
        i += 1

    y = min(sab_textos)

    # Output: assinatura de menor valor
    n3 = len(sab_textos)
    i = 0

    while n3 >= i:
        if sab_textos[i] == y:
            x = i + 1
            i = n3 + 1
        else:
            i += 1

    return print('O autor do texto', x, 'está infectado com COH-PIAH')

def main():
    y = le_assinatura()
    x = le_textos()
    avalia_textos(x, y)
#----------------------------------------------------------------------------
main()