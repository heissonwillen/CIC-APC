tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade
consumo = distancia / 12

print("{:.3f}".format(consumo))