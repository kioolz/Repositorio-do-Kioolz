#Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A
#seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua
#posição dentro do vetor, mostrando esta informação.

#Entrada
#A primeira linha de entrada contém um único inteiro N (1 < N < 1000), indicando o
#número de elementos que deverão ser lidos em seguida para o vetor X[N] de inteiros. A
#segunda linha contém cada um dos N valores, separados por um espaço.

#Saída
#A primeira linha apresenta a mensagem “Menor valor:” seguida de um espaço e do menor
#valor lido na entrada. A segunda linha apresenta a mensagem “Posicao:” seguido de um
#espaço e da posição do vetor na qual se encontra o menor valor lido, lembrando que o
#vetor inicia na posição zero.

import random
from random import randint 


def func(N):

    N = int(input())
    X = []

    if (N > 1) and (N < 1000):
        for i in range(N):
            Z = int(input())
            X.append(Z)        
    else: 
        print("Valor inválido, tente novamente")
    print(X)

    menor = 9999999999999999999999999999999999

    for i in range(N):
        if (menor >  X[i]):
            menor = X[i]

    print("Este é o menor valor", menor)

    for j in range (N):
        if (menor == X[j]):
            print("O menor valor se encontra na posição", j)


    return() 

func(10)

    



    









