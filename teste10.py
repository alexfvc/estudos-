import mega_senafinal as mgf
z = 0
while z != 100:
    z = z + 1
    x = mgf.jogando()
    t = 0
    qd = 0
    qn = 0
    sn = 0
    d = 0
    if x == "terno":
        t = t + 1
    elif x == "quadra":
        qd = qd + 1
    elif x == "quina":
        qn = qn + 1
    elif x == "senna":
        sn = sn + 1
    else:
        d = d + 1
print(f"terno: {t};\nquadra: {qd};\nquina: {qn};\nsenna {sn};\nperdeu: {d}")
    

