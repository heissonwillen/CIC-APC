'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva uma função que recebe uma lista de números e retorna a soma dos números
negativos na lista.
'''

def soma_dos_negativos(numeros):
    return sum([x for x in numeros if x < 0])

print(soma_dos_negativos([-1, -3, -10, 12, 90, -9]))
