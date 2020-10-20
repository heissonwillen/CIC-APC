def mostra(n, invertido=False):
    n = str(n)

    if not invertido:
        print(n, end='')
    else:
        print(n[::-1], end='')

n = int(input())

for i in range(n):
    a, b = [int(j) for j in input().split()]

    for k in range(a, b+1):
        mostra(k)

    for k in range(b, a-1, -1):
        mostra(k, invertido=True)

    print()