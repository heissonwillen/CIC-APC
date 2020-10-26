'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva uma função que recebe uma lista de números inteiros e retorna a quantida
de números ímpares na lista.
'''

def quantidade_de_impares(numeros):
    return len([x for x in numeros if x%2 != 0])

print(quantidade_de_impares([1, 2, 3, 4]))
