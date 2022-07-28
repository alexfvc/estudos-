# probabilidade de vencer
from math import factorial

n = int(21)
c = int(15)
m = 0
p = 0

p = (factorial(n))/((factorial(c)*(factorial(n-c))))


print(f"total de possibilidades {p}")
print(f"sua chance de ganhar {100/p} %")
