def soma_ate(n):
    soma = n*(n+1)//2
    return soma

"""Chamada direta da função
"""
# print(soma_ate(10))
# print(soma_ate(11))

"""Lendo o número da entrada padrão
"""
# n = int(input())
# print(soma_ate(n))

"""Lendo o número da entrada padrão, mas dessa vez compondo mais ainda as funções
"""
print(soma_ate(int(input())))