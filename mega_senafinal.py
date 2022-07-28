import random as rand
import numpy as np

'''esse programa ajudara a saber quantos jogos devem ser feitos para ganharmos a ponto de se parar, 
ou seja, premiação > custo.
(A principio será usado um grupo de 40 numeros para jogar 30 jogos diferentes 
mas isso será revisto para q o usuario escolha a quantidade de numeros e jogos a ser feito.)
'''

totaldenumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                  24, 25]
"""[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                  24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                  49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]""" #lista de numeros da mega para quina use ~>""", 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80"""


def listagem():
    cont = 0
    listade40 = []
    while cont != 22:
        listade40 = [rand.choice(totaldenumeros)] + listade40
        listade40 = set(listade40)
        listade40 = list(listade40)
        cont = int(len(listade40)) + 1

    return listade40


listade40 = listagem()


def cria_jogos(ne=None):  # Cria um jogo (deve ser repetido quantas vezes se fizer necessario)
    cont = 0
    mj = []
    ne = []
    listade40 = (listagem())
    while cont != 16:
        ne = rand.choice(listade40)
        mj.append(ne)
        listade40.remove(ne)  # while interno passa apenas uma vez
        # deveria passar 30 vezes para criar jogos diferentes
        cont = int(len(mj)) + 1
        mj.sort()

    return mj


lj = []  # lista de jogos
# quantidade de jogos na lista(quantos jogos esetao sendo feitos nos 40 numeros)
qj = 0
while qj != 220:
    mj = cria_jogos()
    lj.append(mj)
    qj = qj + 1

    # 30 jogos criados


# simulacao de sorteio

def jogando():
    jogo = (cria_jogos())

    
    print(jogo)
    print('------' * 10)
    premio = 0
    for x in lj:
        c1 = 0

        if jogo[0] in x:

            c1 = c1 + 1
        if jogo[1] in x:


            c1 = c1 + 1
        if jogo[2] in x:

            c1 = c1 + 1
        if jogo[3] in x:

            c1 = c1 + 1
        if jogo[4] in x:

            c1 = c1 + 1
        if jogo[5] in x:

            c1 = c1 + 1
        if jogo[6] in x:

            c1 = c1 + 1
        if jogo[7] in x:

            c1 = c1 + 1
        if jogo[8] in x:

            c1 = c1 + 1
        if jogo[9] in x:

            c1 = c1 + 1
        if jogo[10] in x:

            c1 = c1 + 1
        if jogo[11] in x:

            c1 = c1 + 1
        if jogo[12] in x:

            c1 = c1 + 1
        if jogo[13] in x:

            c1 = c1 + 1
        if jogo[14] in x:

            c1 = c1 + 1





        if c1 == 11:
            print(x)
            print("11")
            print("^^^^^^" * 10)
            premio = premio + 5
        if c1 == 12:
            print(x)
            print("12")
            print("^^^^^^" * 10)
            premio = premio + 10
        if c1 == 13:
            print(x)
            print("13")
            print("^^^^^^" * 10)
            premio = premio + 25
        if c1 == 14:
            print(x)
            print("14")
            print("^^^^^^" * 10)
            premio = premio + 950
        if c1 == 15:
            print(x)
            print("15")
            print("^^^^^^" * 10)
            premio = premio + 1000000
        if c1 == 11 or c1 ==12 or c1 == 13 or c1 == 14 or c1 == 15:
            print('_______' * 5)
    print(premio)
jogando()

