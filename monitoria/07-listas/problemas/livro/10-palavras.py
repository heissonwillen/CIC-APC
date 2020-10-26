'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva uma função que recebe uma lista de palavras (strings) e retorna o número
de palavras na lista que tem comprimento 5.
'''

def numero_de_palavras(palavras):
    return len([p for p in palavras if len(p) == 5])

print(numero_de_palavras(['oi', 'saude', 'carne', 'batata']))
