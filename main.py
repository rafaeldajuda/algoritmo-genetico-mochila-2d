from gen import *
import copy

# teste
plano_teste_5 = [[1,1,3,3,3],
                 [2,2,3,3,3],
                 [2,2,3,3,3],
                 [0,0,1,2,2],
                 [0,0,0,2,2]]

plano_teste_6 = [[1,1,2,2,2,2],
                 [0,0,2,2,2,2],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]

### definição do plano
DIMENSAO_3X3 = 3
DIMENSAO_4X4 = 4
DIMENSAO_5X5 = 5
DIMENSAO_6X6 = 6

CAIXAS = {
    1 : 1,
    2 : 4,
    3 : 9
}

dimensao = DIMENSAO_3X3
plano = criar_plano(dimensao) 
# plano = plano_teste_5

# ver_plano(plano, dimensao)

### solução exata (força bruta)
solucoes = []

# for _ in range(25000):
#     # preenchimento
#     plano = criar_plano(dimensao) 
#     novo_plano = preencher_plano(plano, dimensao, CAIXAS)

#     print('Novo plano\n')
#     ver_plano(novo_plano, dimensao)
#     print()

#     # guardar solução
#     solucao = []
#     for x in novo_plano:
#         for ponto in x:
#             solucao.append(ponto)
#     if solucao not in solucoes:
#         solucoes.append(solucao)

# print(f'solucoes: {len(solucoes)}')
# print(solucoes)

caixas = [1,2,3]
ver_plano(plano)
print()

planos = []

def teste(plano, caixas):
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
                teste(novo_plano, caixas)
    return False
            
teste(plano, caixas)
print(planos)

print()
print('solucoes')
print(solucoes)


### soluçao heurística
