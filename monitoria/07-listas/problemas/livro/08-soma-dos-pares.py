'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva uma função que recebe uma lista de números inteiros e retorna a soma dos
números pares na lista.
'''

def soma_dos_pares(numeros):
    return sum([x for x in numeros if x%2 == 0])

print(soma_dos_pares([2, 2, 2, 9, 9]))
