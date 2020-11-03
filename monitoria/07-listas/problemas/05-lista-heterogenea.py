'''
Dada uma lista heterogênea, definir uma função que retorna uma nova lista
que contém somente os valores inteiros da lista inicial.
'''

def somente_inteiros(lista_mista):
    nova_lista = list()
    for item in lista_mista:
        if isinstance(item, int):
            nova_lista.append(item)
    return nova_lista

def somente_do_tipo(lista_mista, tipo):
    nova_lista = list()
    for item in lista_mista:
        if isinstance(item, tipo):
            nova_lista.append(item)
    return nova_lista

def somente_do_tipo(lista_mista, tipo):
    return [item for item in lista_mista if isinstance(item, tipo)]

lista = [10, 22.2, "Nome", "Outro nome", 11]

# print(somente_inteiros(lista))
print(somente_do_tipo(lista, str))
