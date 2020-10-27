'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva uma função soma_de_quadrados(xs) que recebe uma lista de números xs e
retorna a soma dos quadrados dos números na lista.
Por exemplo soma_dos_quadrados([2, 3, 4]) deve retorna 4+9+16 que é 29.
'''

def soma_de_quadrados(numeros):
    return sum([x**2 for x in numeros])

print(soma_de_quadrados([2, 3, 4]))
