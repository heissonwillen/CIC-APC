'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva uma função que recebe a lista de inteiros do exercício anterior e
retorna o maior valor na lista. (Observação: existe uma a função nativa max que
faz o serviço, mas você não deve usá-la.)
'''

def maior_valor(lista):
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

print(maior_valor([1, 4, 90, -10]))
