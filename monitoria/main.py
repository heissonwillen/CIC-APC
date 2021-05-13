# with open('saida6.txt', 'r') as arquivo_gabarito, open('ester.txt') as arquivo_saida:
#     linhas_gabarito = arquivo_gabarito.readlines()
#     linhas_saida = arquivo_saida.readlines()

#     for linha_gabarito, linha_saida in zip(linhas_gabarito, linhas_saida):
#         if not linha_gabarito == linha_saida:
#             print('erro')


# tamanho do vetor
inteiros = []
n = int(input())

# elementos do vetor

lista = input().split()
for i in lista:
    inteiros.append(int(i))

# quantidade de perguntas:
q = int(input())

registros = {}

indice = 0

for inteiro in inteiros:
    if inteiro not in registros:
        registros[inteiro] = [0, 'x']
    registros[inteiro][0] += 1
    if registros[inteiro][1] == 'x':
        registros[inteiro][1] = indice
    indice += 1

while q > 0:
    x, y = (int(x) for x in input().split())
    if x == 1:
        if y in registros:
            print(registros[y][0])
        else:
            print('-1')
    elif x == 2:
        if y in registros:
            print(registros[y][1])
        else:
            print('-1')
    q -= 1
