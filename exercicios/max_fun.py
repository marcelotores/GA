#Exercício 1:
#Implemente um algoritmo genético simples para maximizar a função f(x) = x^2 
#no intervalo de -10 a 10. Considere uma população inicial de 10 indivíduos 
#e execute o algoritmo por 5 gerações.

#START
#Generate the initial population
#Compute fitness
#REPEAT
#    Selection
#    Crossover
#    Mutation
#    Compute fitness
#UNTIL population has converged
#STOP

from numpy.random import randint
from numpy.random import rand
import numpy as np
import random

tamanho_populacao = 10
aptidao = []

random.seed(0)
populacao = [random.randint(-10, 10) for _ in range(tamanho_populacao)]


def funcao_objetivo(x):
    return x**2

def algoritmo_genetico():
    for cromossomo in populacao:
        aptidao.append(funcao_objetivo(cromossomo))
        
    print('aptidao: ', aptidao)

    aptidao_order = sorted(aptidao, reverse=True)
    print(aptidao_order)

print(populacao)
algoritmo_genetico()






