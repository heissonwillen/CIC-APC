'''
Definir a função 'remove_repetidos' que, dada uma lista, retorna uma lista sem elementos repetidos.

Exemplos:
print(remove_repetidos(['Brasilia', 'Goiania', 'Caxias', 'Rio de Janeiro', 'Belo Horizonte', 'Brasilia', 'Goiania', 'Goiania']))
>>> ['Brasilia', 'Goiania', 'Caxias', 'Rio de Janeiro', 'Belo Horizonte']
print(remove_repetidos(1, 1, 1, 1, 1, 1, 1, 2, 2, 2))
>>> [1, 2]
'''

def remove_repetidos(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista


print(remove_repetidos(['Brasilia', 'Goiania', 'Caxias', 'Rio de Janeiro', 'Belo Horizonte', 'Brasilia', 'Goiania', 'Goiania']))
print(remove_repetidos([1, 1, 1, 1, 1, 1, 1, 2, 2, 2]))
