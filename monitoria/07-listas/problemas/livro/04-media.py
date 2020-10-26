'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Crie uma lista contendo 100 números inteiros aleatórios entre 0 e 1000 (usando
iteração, "append" e o módulo random). Escreva uma função media que recebe uma
lista de números como parâmetros e retorna a média dos valores na lista.
'''

from random import uniform

# def media(numeros):
#     soma = 0
#     num_itens = 0
#
#     for numero in numeros:
#         soma += numero
#         num_itens += 1
#
#     media = soma/num_itens
#     return media

def media(numeros):
    return sum(numeros)/len(numeros)

numeros = []
for i in range(10):
    numeros.append(int(uniform(0, 1000)))

print(numeros)
print(media(numeros))
