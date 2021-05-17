n, x = [int(i) for i in input().split()]

cartazes = [int(i) for i in input().split()]
pontos = [cartazes[0]] + [int(i) for i in input().split()]

dicio_cartazes = {}
for i, cartaz in enumerate(cartazes):
    dicio_cartazes[cartaz] = i

total = 0
for i in range(len(pontos[:-1])):
    total += abs(dicio_cartazes[pontos[i]] - dicio_cartazes[pontos[i+1]])

print(total)


# n1, n2 = map(int, input().split())
# lista = list(map(int, input().split()))
# elementos = list(map(int, input().split()))
# anterior = 0
# posicao = 0
# for i in range(len(elementos)):
#     valor = lista.index(elementos[i])
#     posicao += abs(valor-anterior)
#     anterior = valor
# print(int(posicao))
