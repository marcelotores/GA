import random

# Parâmetros do algoritmo genético
populacao_tamanho = 10
tamanho_cromossomo = 6
taxa_mutacao = 0.1
numero_geracoes = 100

# Função de aptidão (fitness function)
def calcular_aptidao(cromossomo):
    objetivo = [1, 0, 1, 1, 0, 1]  # Cromossomo objetivo
    aptidao = 0
    for i in range(tamanho_cromossomo):
        if cromossomo[i] == objetivo[i]:
            aptidao += 1
    return aptidao

# Função de mutação
def mutacao(cromossomo):
    for i in range(tamanho_cromossomo):
        if random.random() < taxa_mutacao:
            cromossomo[i] = 1 - cromossomo[i]
    return cromossomo

# Gerar uma população inicial aleatória
populacao = []
for _ in range(populacao_tamanho):
    cromossomo = [random.randint(0, 1) for _ in range(tamanho_cromossomo)]
    populacao.append(cromossomo)


# Executar o algoritmo genético
for geracao in range(numero_geracoes):
    print(f"=== Geração {geracao+1} ===")
    aptidoes = [calcular_aptidao(cromossomo) for cromossomo in populacao]
    ## Ao final haverá um lista de aptidões (um aptidão para cada cromo da população)
 
    # Mostrar a população atual
    for i in range(populacao_tamanho):
        print(f"Cromossomo {i+1}: {populacao[i]}, Aptidão: {aptidoes[i]}")

    # Seleção dos pais
    pais = random.choices(populacao, weights=aptidoes, k=2)
    # Seleciona os pais que irão cruzar. A função choices recebe a probabilidade de cada valor 
    # ser escolhido pelo parâmetro weichts. k representa a quantidade de elementos escolhidos.
    # dessa forma, os cromossomos daquela população com maior aptidão terão maior chance de serem
    # escolhidos.
 
    # Cruzamento (reprodução)
    filho = []
    for i in range(tamanho_cromossomo):
        pai = random.choice(pais)
        filho.append(pai[i])

    # faz o cruzamento entre os pais. 1º escolhe um de dois pais (aleatoriamente) e pega aquele gene
    # (bit) para compor o filho naquela iteração, e assim sucessivamente. Não mantém um padrão
    # de escoha dos bits de quais pais. Assim, um filho pode em os dois primeiros bits de um dos pais
    # e o outro cromossomo pode ter os 3 primeiros.

    # Mutação
    filho = mutacao(filho)

    # Substituir o pior indivíduo da população pelo filho
    indice_pior = min(range(populacao_tamanho), key=lambda i: aptidoes[i])
    populacao[indice_pior] = filho
    ## Substitui o pior cromossomo daquela população pelo filho

print("\n=== Resultado Final ===")
aptidoes = [calcular_aptidao(cromossomo) for cromossomo in populacao]
for i in range(populacao_tamanho):
    print(f"Cromossomo {i+1}: {populacao[i]}, Aptidão: {aptidoes[i]}")
