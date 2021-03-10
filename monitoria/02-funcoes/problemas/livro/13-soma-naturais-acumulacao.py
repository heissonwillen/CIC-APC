def soma_ate(n):
    s = 0
    for i in range(n+1):
        s += i
    return s

# def soma_ate(n):
#     contador = 1
#     soma = 0
#     while contador <= n:
#         soma = soma + contador
#         contador = contador + 1

#     return soma

print(soma_ate(10))