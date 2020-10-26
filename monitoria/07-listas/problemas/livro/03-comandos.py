'''
https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html

Escreva comandos para:
Inserir “pera” e 76 no final da lista.
Inserir o valor “gato” na posição de índice 3.
Inserir o valor 99 no início da lista.
Encontrar o índice de “oi”.
Contar o número de ocorrências de 76 na lista.
Remover a primeira ocorrência de 76 da lista.
Remover True True da lista usando pop e index.
'''

minha_lista = []
minha_lista.append(pera)
minha_lista.append(76)
minha_lista.insert(3, "gato")
minha_lista.insert(0, "gato")
minha_lista.index("oi")
minha_lista.count(76)
minha_lista.remove(76)
minha_lista.pop(minha_lista.index(76))
