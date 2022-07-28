#probabilidade de vencer
from math import factorial
import random
a =  int()
cont = 1
while a != 1:
    a = random.randrange(1, 60, 1)
    print(a)
    if a != 1:
        cont = cont + 1
    else:
        print(f"numero de vezes {cont}")