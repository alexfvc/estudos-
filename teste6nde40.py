#numeros de jogos para ganhar
import random
import numpy as np
                                            #passo:zero nomear as variaveis
ca1 = 0
ca2 = 0
ca3 = 0
ca4 = 0
ca5 = 0
ca6 = 0
cat = 0
                                             #passo 1: fazer meu jogo

mj = np.random.randint(1, 61, (40,6))

mj = list(map(list, mj))

mj[0].sort()
mj[1].sort()
mj[2].sort()
mj[3].sort()
mj[4].sort()
mj[5].sort()
mj[6].sort()
mj[7].sort()
mj[8].sort()
mj[9].sort()
mj[10].sort()
mj[11].sort()
mj[12].sort()
mj[13].sort()
mj[14].sort()
mj[15].sort()
mj[16].sort()
mj[17].sort()
mj[18].sort()
mj[19].sort()
mj[20].sort()
mj[21].sort()
mj[22].sort()
mj[23].sort()
mj[24].sort()
mj[25].sort()
mj[26].sort()
mj[27].sort()
mj[28].sort()
mj[29].sort()
mj[30].sort()
mj[31].sort()
mj[32].sort()
mj[33].sort()
mj[34].sort()
mj[35].sort()
mj[36].sort()
mj[37].sort()
mj[38].sort()
mj[39].sort()

"""
new = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], k = 40)
new.sort()

new = set(new)
new = list(new)
print(len(new))
"""
print(mj)


                                             #passo 2: jogo do computador    
                                                                                   
a1 = random.randrange(1, 61, 1)            
a2 = random.randrange(1, 61, 1)
a3 = random.randrange(1, 61, 1)
a4 = random.randrange(1, 61, 1)
a5 = random.randrange(1, 61, 1)
a6 = random.randrange(1, 61, 1)
jogo = [a1, a2, a3, a4, a5, a6]
jogo.sort()
                                             #passo 3: valida-lo o jogo e contar

print(jogo)

if (a1 == a2 or a1 == a3 or a1 == a4 
or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 
or a2 == a5 or a2 == a6 or a3 == a4 or a3 == a5 
or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6):
    print("numero repetido, jogo invalido")
    
elif jogo in mj :
    print(f"voce esta milhonario {jogo}")
    
else:
    if jogo[0] in mj[0] or mj[1] or mj[2] or mj[3] or mj[4] or mj[5] or mj[6] or mj[7] or mj[8] or mj[9] or mj[10] or mj[11] or mj[12] or mj[13] or mj[14] or mj[15] or mj[16] or mj[17] or mj[18] or mj[19] or mj[20] or mj[21] or mj[22] or mj[23] or mj[24] or mj[25] or mj[26] or mj[27] or mj[28] or mj[29] or mj[30] or mj[31] or mj[32] or mj[33] or mj[34] or mj[35] or mj[36] or mj[37] or mj[38] or mj[39]:
        cat = cat +1
    if jogo[1] in mj[0] or mj[1] or mj[2] or mj[3] or mj[4] or mj[5] or mj[6] or mj[7] or mj[8] or mj[9] or mj[10] or mj[11] or mj[12] or mj[13] or mj[14] or mj[15] or mj[16] or mj[17] or mj[18] or mj[19] or mj[20] or mj[21] or mj[22] or mj[23] or mj[24] or mj[25] or mj[26] or mj[27] or mj[28] or mj[29] or mj[30] or mj[31] or mj[32] or mj[33] or mj[34] or mj[35] or mj[36] or mj[37] or mj[38] or mj[39]:
        cat = cat +1
    if jogo[2] in mj[0] or mj[1] or mj[2] or mj[3] or mj[4] or mj[5] or mj[6] or mj[7] or mj[8] or mj[9] or mj[10] or mj[11] or mj[12] or mj[13] or mj[14] or mj[15] or mj[16] or mj[17] or mj[18] or mj[19] or mj[20] or mj[21] or mj[22] or mj[23] or mj[24] or mj[25] or mj[26] or mj[27] or mj[28] or mj[29] or mj[30] or mj[31] or mj[32] or mj[33] or mj[34] or mj[35] or mj[36] or mj[37] or mj[38] or mj[39]:
        cat = cat +1
    if jogo[3] in mj[0] or mj[1] or mj[2] or mj[3] or mj[4] or mj[5] or mj[6] or mj[7] or mj[8] or mj[9] or mj[10] or mj[11] or mj[12] or mj[13] or mj[14] or mj[15] or mj[16] or mj[17] or mj[18] or mj[19] or mj[20] or mj[21] or mj[22] or mj[23] or mj[24] or mj[25] or mj[26] or mj[27] or mj[28] or mj[29] or mj[30] or mj[31] or mj[32] or mj[33] or mj[34] or mj[35] or mj[36] or mj[37] or mj[38] or mj[39]:
        cat = cat +1
    if jogo[4] in mj[0] or mj[1] or mj[2] or mj[3] or mj[4] or mj[5] or mj[6] or mj[7] or mj[8] or mj[9] or mj[10] or mj[11] or mj[12] or mj[13] or mj[14] or mj[15] or mj[16] or mj[17] or mj[18] or mj[19] or mj[20] or mj[21] or mj[22] or mj[23] or mj[24] or mj[25] or mj[26] or mj[27] or mj[28] or mj[29] or mj[30] or mj[31] or mj[32] or mj[33] or mj[34] or mj[35] or mj[36] or mj[37] or mj[38] or mj[39]:
        cat = cat +1
    if jogo[5] in mj[0] or mj[1] or mj[2] or mj[3] or mj[4] or mj[5] or mj[6] or mj[7] or mj[8] or mj[9] or mj[10] or mj[11] or mj[12] or mj[13] or mj[14] or mj[15] or mj[16] or mj[17] or mj[18] or mj[19] or mj[20] or mj[21] or mj[22] or mj[23] or mj[24] or mj[25] or mj[26] or mj[27] or mj[28] or mj[29] or mj[30] or mj[31] or mj[32] or mj[33] or mj[34] or mj[35] or mj[36] or mj[37] or mj[38] or mj[39]:
        cat = cat +1
   

print(cat)
    
if cat == 5:
    print('probabilidade de quina')
        
elif cat == 4:
    print('probabilidade de quadra')
        
elif cat == 3:
    print('probabilidade de terno')
        
else:
    print("se lascou")
        

print(f'total de numeros que saira {cat}')
print("--------"*10)


'''
mj[0]
mj[1]
mj[2]
mj[3]
mj[4]
mj[5]
mj[6]
mj[7]
mj[8]
mj[9]
mj[10]
mj[11]
mj[12]
mj[13]
mj[14]
mj[15]
mj[16]
mj[17]
mj[18]
mj[19]
mj[20]
mj[21]
mj[22]
mj[23]
mj[24]
mj[25]
mj[26]
mj[27]
mj[28]
mj[29]
mj[30]
mj[31]
mj[32]
mj[33]
mj[34]
mj[35]
mj[36]
mj[37]
mj[38]
mj[39]
'''