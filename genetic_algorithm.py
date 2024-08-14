import random

def criar_plano(dimensao):
    plano = []
    for i in range(dimensao):
        x = []
        for j in range(dimensao):
            x.append(0)
        plano.append(x)
    
    return plano

def ver_plano(plano, dimensao):
    for i in plano:
        x = ''
        for j in i:
            x = x + str(j) + '  '
        print(f'{x}')

def preencher_plano(plano, dimensao, CAIXAS):
    # preenchimento
    count = 0
    while True:
        # pegando caixa aleatória
        caixa = random.randint(1, 3)
        caixa_area = CAIXAS[caixa]

        # teste
        # caixa = 2
        # caixa_area = CAIXAS[caixa]

        print(f'count: {count}')
        ver_plano(plano, dimensao)

        # chechando se existe espaco para colocar a caixa
        existe_espaco = False    
        sequencia_zeros_linhas = 0
        posicao_linha = -1
        posicao = -1
        print(f'caixa: {caixa}')
        
        for key, x in enumerate(plano):
            if x.count(0) >= caixa:
                sequencia_zeros = 0
                for key_celula, value_celula in enumerate(x):
                    if value_celula == 0:
                        if x[key_celula:key_celula+caixa].count(0) == caixa and posicao == -1:
                            posicao = key_celula
                            posicao_linha = key
                            sequencia_zeros_linhas = sequencia_zeros_linhas + 1
                            break
                        if x[key_celula:key_celula+caixa].count(0) == caixa and posicao == key_celula:
                            sequencia_zeros_linhas = sequencia_zeros_linhas + 1
                            break
                        elif posicao == key_celula:
                            sequencia_zeros_linhas = 0
                            break
            else:
                sequencia_zeros_linhas = 0
            if sequencia_zeros_linhas == caixa:
                existe_espaco = True
                break
        # fim for
        print(f'existe_espaco: {existe_espaco}')

        # colando uma caixa no plano
        plano_aux = plano
        
        if existe_espaco:
            count_total = 0
            for key_x, value_x in enumerate(plano):
                count_linha = 0
                pular_linha = True
                if value_x.count(0) >= caixa and key_x >= posicao_linha:
                    for key_celula, value_celula in enumerate(value_x):
                        if value_x[key_celula:key_celula+caixa].count(0) == caixa and posicao == key_celula or not pular_linha:
                            if posicao == key_celula:
                                pular_linha = False
                            if pular_linha:
                                continue

                            plano_aux[key_x][key_celula] = caixa
                            count_linha = count_linha + 1
                            if count_linha == caixa:
                                count_total = count_total +1
                                break
                    # fim for
                # fim if

                if count_total == caixa:
                    break
            # fim for
        # fim if
        
        # guardar novo plano
        plano = plano_aux

        # checa se todo plano foi preenchido
        count_plano_cheio = 0
        for x in plano:
            if x.count(0) == 0:
                count_plano_cheio = count_plano_cheio + 1 

        # limitar loop
        count = count + 1
        if count > 50 or count_plano_cheio ==  dimensao:
            break
    # fim while

    return plano
