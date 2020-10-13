from math import sqrt

def distancia(x_1, y_1, x_2, y_2):
    return sqrt((x_2-x_1)**2+(y_2-y_1)**2)

x_b, y_b = [int(x) for x in input().split()]

menor_distancia = 0
mais_perto = 0

for i in range(3):
    x, y = [int(x) for x in input().split()]
    d = distancia(x_b, y_b, x, y)

    if i == 0 or d < menor_distancia:
        menor_distancia = d
        mais_perto = i+1

print(mais_perto)
