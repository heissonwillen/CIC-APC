'''
[<expressão> for <item> in <sequência> if <condição>]
'''


def nested_sum(lista):
    return sum([sum(sub_lista) for sub_lista in lista])

def nested_sum(lista):
    soma = 0
    for sub_lista in lista:
        soma += sum(sub_lista)
    return sum(sub_lista)

    def nested_sum(lista):
        soma = 0
        for sub_lista in lista:
            soma += sum(sub_lista)
        return soma


# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))
