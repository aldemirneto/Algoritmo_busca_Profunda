def procura( caminho, x:int, y:int, encontra:int):
    if x == 4 and y == 4:
        encontra = 1
        return 1
    if y < 4:
        if caminho[y+1][x] != 1:
            caminho[y][x] = 1
            return procura(caminho, x, y+1, encontra)
    if x < 4:
        if caminho[y][x+1] != 1:
            caminho[y][x] = 1
            return procura(caminho, x+1, y, encontra)
    if x > 0:
        if caminho[y][x-1] != 1:
            caminho[y][x] = 1
            return procura(caminho, x-1, y, encontra)
    if y > 0:
        if caminho[y-1][x] != 1:
            caminho[y][x] = 1
            return procura(caminho, x, y - 1, encontra)
    if caminho[0][0] == 1:
        return 0
    else:
        return 0





T = int(input())
encontra = 0
x, y = 0, 0
respostas = []

for t in range(T):
    caminho = []
    k = 0
    while k < 5:
        temp = input().split()
        if temp:
            caminho.append(list(map(int, temp)))
            k += 1
    if encontra == 1:
        respostas.append('COPS')
    else:
        respostas.append('ROBBERS')

for i in range(len(respostas)):
    print(respostas[i])