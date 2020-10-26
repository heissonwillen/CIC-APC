'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Apesar de Python nós fornecer uma grande lista de métodos nativos é uma boa
prática e instrutivo pensar sobre como elas podem ser implementadas. Implemente
uma função que se comporte como:

count
in
reverse
index
insert
'''

def numero_de_ocorrencias(procurado, lista):
    total = 0
    for elemento in lista:
        if elemento == procurado:
            total += 1
    return total

def esta_contido(procurado, lista):
    for elemento in lista:
        if elemento == procurado:
            return True
    return False

def ao_contrario(lista):
    nova_lista = []
    for i in range(len(lista)-1, -1, -1):
        nova_lista.append(lista[i])
    return nova_lista

def indice_de(procurado, lista):
    for indice, elemento in enumerate(lista):
        if elemento == procurado:
            return indice
    return -1

def inserir(elemento, posicao, lista):
    return lista[:posicao] + [elemento] + lista[posicao:]


lista_1 = [10, 10, 11, 89]
lista_2 = [True, 10.9, '11', 'casa']

# print(numero_de_ocorrencias(10, lista_1))
# print(numero_de_ocorrencias('batata', lista_2))

# print(esta_contido(10, lista_1))
# print(esta_contido('batata', lista_2))

# print(ao_contrario(lista_1))
# print(ao_contrario(lista_2))

# print(indice_de(10, lista_1))
# print(indice_de('batata', lista_2))

# print(inserir(9, 1, lista_1))
# print(inserir('foguete', 3, lista_2))
