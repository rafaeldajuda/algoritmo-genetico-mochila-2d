

from genetic_algorithm import *

# teste
plano_teste_5 = [[1,1,3,3,3],
                 [2,2,3,3,3],
                 [2,2,3,3,3],
                 [0,0,1,2,2],
                 [0,0,0,2,2]]

plano_teste_6 = [[1,1,2,2,2,2 ],
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

dimensao = DIMENSAO_4X4
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
numero_inicial = [3]
print(f'numero_inicial: {numero_inicial}\n')
ver_plano(plano, dimensao)

posicoes_de_inicio = pegar_posicoes_iniciais(dimensao, numero_inicial)
print()
print(posicoes_de_inicio)
plano_inicial = preencher_plano_inicial(dimensao, posicoes_de_inicio)

def colocar_caixa(caixas, planos):
    

    return


### soluçao heurística
