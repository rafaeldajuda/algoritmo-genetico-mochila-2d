from gen import *
import datetime

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

caixas = [1,2,3]
ver_plano(plano)
print()

planos = []

print(datetime.datetime.now())
preencher_planos(plano, caixas, planos)
print(datetime.datetime.now())
print(planos)
print(len(planos))

print()
print('solucoes')
print(solucoes)


### soluçao heurística
