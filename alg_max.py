import random

def funcao_objetivo(x):
    return x**2

def algoritmo_genetico():
    # Configurações do algoritmo genético
    tamanho_populacao = 10
    geracoes = 5
    
    # Inicialização da população com valores aleatórios
    populacao = [random.randint(-10, 10) for _ in range(tamanho_populacao)]
    print(populacao)
    # Loop das gerações
    for _ in range(geracoes):
        # Avaliação da aptidão de cada indivíduo na população
        aptidoes = [funcao_objetivo(individuo) for individuo in populacao]
        print(aptidoes)
        # Seleção dos indivíduos mais aptos
        melhores_individuos = sorted(range(len(aptidoes)), key=lambda i: aptidoes[i], reverse=True)[:2]

        # Exibição dos melhores indivíduos
        for indice in melhores_individuos:
            print(f"Indivíduo: {populacao[indice]}, Aptidão: {aptidoes[indice]}")

        # Reprodução e crossover
        filhos = []
        for _ in range(tamanho_populacao - len(melhores_individuos)):
            pai1 = random.choice(melhores_individuos)
            pai2 = random.choice(melhores_individuos)
            filho = (populacao[pai1] + populacao[pai2]) / 2
            filhos.append(filho)

        # Mutação
        for i in range(len(filhos)):
            if random.random() < 0.1:  # Probabilidade de mutação: 10%
                filhos[i] = random.randint(-10, 10)

        # Atualização da população
        populacao = melhores_individuos + filhos

# Execução do algoritmo genético
algoritmo_genetico()
