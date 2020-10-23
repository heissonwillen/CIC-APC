n = int(input())

for _ in range(n):
    lista = input().split()
    lista.sort(key=lambda item: len(item), reverse=True)

    for i in range(len(lista)):
        print(lista[i], end='')
        if i != len(lista)-1:
            print(' ', end='')

    print()
