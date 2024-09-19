import random
import copy

def criar_plano(dimensao):
    plano = []
    for i in range(dimensao):
        x = []
        for j in range(dimensao):
            x.append(0)
        plano.append(x)
    
    return plano

def ver_plano(plano):
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

def existe_espaco(caixa, plano, linha, coluna):
    for i in range(caixa):
        for j in range(caixa):
            if i+linha >= len(plano) or j+coluna >= len(plano[0]) or plano[i+linha][j+coluna] != 0:
                return False
            
    return True

def pegar_posicoes_iniciais(dimensao, numero_inicial):
    posicoes = []
    for _, v in enumerate(numero_inicial):
        for i in range(dimensao):
            for j in range(dimensao):
                if i + v <= dimensao and j+v <= dimensao:
                    posicao = {}
                    posicao['caixa'] = v
                    posicao['x'] = i
                    posicao['y'] = j
                    posicoes.append(posicao)

    return posicoes

def preencher_plano_inicial(dimensao, posicoes):
    planos = []

    for _, posicao in enumerate(posicoes):
        plano = criar_plano(dimensao)

        # preencher
        for i in range(posicao['caixa']):
            for j in range(posicao['caixa']):
                    x = posicao['x']+i
                    y = posicao['y']+j
                    plano[x][y] = posicao['caixa']
        # fim for

        planos.append(plano)
    # fim for

    return planos

def colocar_caixa(caixa, p, linha, coluna):
    for i in range(caixa):
        for j in range(caixa):
            p[i+linha][j+coluna] = caixa

    return p


def plano_cheio(plano):
    # checa se todo plano foi preenchido
    count_zeros = 0
    for x in plano:
        if x.count(0) == 0:
            count_zeros = count_zeros + 1
    if count_zeros == len(plano):
        return True
    return False

def preencher_planos(plano, caixas, planos):
    ver_plano(plano)
    print()
    for linha in range (len(plano)):
        for coluna in range (len(plano[0])):

            for _, caixa in enumerate(caixas):
                print('caixa:', caixa)
                print('linha:', linha)
                print('coluna', coluna)
                espaco = existe_espaco(caixa, plano, linha, coluna)
                print('espaco', espaco)
                if not espaco:
                    continue

                # preencher uma celula
                novo_plano = copy.deepcopy(plano)
                novo_plano = colocar_caixa(caixa, novo_plano, linha, coluna)
                ver_plano(novo_plano)
                print()
                fim = plano_cheio(novo_plano)
                if fim and novo_plano not in planos:
                    print("plano_cheio:", fim)
                    planos.append(novo_plano)
                    return True
                if len(planos) == 10:
                    return True
                preencher_planos(novo_plano, caixas, planos)
    return False

