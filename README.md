# Problema: Preenchimento de Plano 2D com Máxima Pontuação

## Descrição Geral

Você deve desenvolver um algoritmo que preencha um plano de duas dimensões dividido em quadrantes de tamanhos variados (3x3, 4x4 e 5x5). O objetivo é preencher esses quadrantes com "caixas" de diferentes dimensões (1x1, 2x2 e 3x3), de forma a maximizar a pontuação total.

## Regras do Problema

1. Dimensões do Plano:
    * O plano pode ter as seguintes dimensões: 3x3, 4x4 e 5x5.

2. Tipos de Caixas e suas Pontuações:
    * Caixas 1x1: valem 1 ponto cada.
    * Caixas 2x2: valem 5 pontos cada.
    * Caixas 3x3: valem 10 pontos cada.

3. Objetivo:
    * Preencher os quadrantes do plano de forma a obter a pontuação máxima possível.

## Restrições

1. As caixas não podem se sobrepor.
2. Cada caixa deve estar totalmente dentro do plano (não pode exceder as bordas do plano).
3. Deve-se considerar soluções exatas e heurísticas.

## Métodos de Solução

1. Soluções Exatas:
    * Exploração exaustiva de todas as combinações possíveis para encontrar a solução ótima.
2. Soluções Heurísticas:
    * Utilização de algoritmos genéticos para encontrar soluções aproximadas de forma mais eficiente.
    * Implementação de funções de fitness para avaliar a qualidade das soluções.

## Implementação e Registro

1. Registro das Soluções:
    * Cada solução encontrada deve ser registrada, incluindo a configuração do preenchimento e a pontuação total obtida.

2. Interface Gráfica:
    * Utilizar Pygame para criar uma interface gráfica que visualize o preenchimento do plano.
    * Mostrar o plano dividido em quadrantes, as caixas colocadas e a pontuação total de cada configuração.

## Passos para a Implementação

1. Definição do Plano:
    * Criação de uma representação do plano 2D (matriz de 3x3, 4x4 ou 5x5).

2. Algoritmo de Preenchimento:
    * Desenvolver funções para colocar caixas de 1x1, 2x2 e 3x3 nos quadrantes.
    * Garantir que as regras de não sobreposição e encaixe dentro do plano sejam respeitadas.

3. Algoritmos Genéticos:
    * Implementar a geração inicial de populações de soluções.
    * Desenvolver operadores de seleção, crossover e mutação.
    * Avaliar a função de fitness baseada na pontuação total das configurações.

4. Registro das Soluções:
    * Criar um mecanismo para registrar e armazenar todas as soluções encontradas, juntamente com suas pontuações.

5. Interface Gráfica com Pygame:
    * Desenhar o plano e as caixas conforme as soluções são geradas.
    * Atualizar a visualização conforme novas soluções são encontradas.
    * Mostrar a pontuação total de cada configuração na interface.

--------------------------

# Prompt ChatGPT

Estou estudando algoritmos genéticos, me ajuda a elaborar o seguinte problema:

* Crie um problema onde é preciso preecher um plano de duas dimenções divididas por quadrantes (3x3, 4x4 e 5x5).
* Os quadrantes precisam ser preenchidos por "caixas" das seguintes dimensões: 1x1, 2x2 e 3x3.
* Cada "caixa" possui uma pontuação:
    * 1x1 vale 1 ponto.
    * 2x2 vale 5 pontos.
    * 3x3 valoe 10 pontos.
* A solução do problema é conseguir preencher os quadrantes com o máximo de pontos possível.
* É preciso utilizar soluções exatas e heurísticas.
* A cada solução encontrada é preciso ser logada.
* É preciso criar uma interface gráfica com pygame para a visualização do problema.
* Não faça a solução em código, só é preciso elaborar o problema em texto.