def pao(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        n = pao(n-1) + pao(n-2)
        return n


posi = int(input("Qual a posição?"))
print(pao(posi))
