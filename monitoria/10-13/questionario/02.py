soma_inversos = 0
quantidade_de_notas = 0

while True:
    nota = int(input())

    if nota == -1:
        break

    soma_inversos += 1/nota
    quantidade_de_notas += 1

print(int(quantidade_de_notas/soma_inversos))
