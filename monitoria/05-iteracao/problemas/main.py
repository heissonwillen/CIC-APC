# def tem_q_somar_os_digitos(x, q=1):
#     if len(str(x)) == 1:
#         return x, q
#     return tem_q_somar_os_digitos(sum(map(int, str(x))), q+1)


# print(tem_q_somar_os_digitos(159))
# print(tem_q_somar_os_digitos(1239871239781946102731089298))
# print(tem_q_somar_os_digitos(7))

# def contagem_divisores(n):
#     quantidade_divisores = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             quantidade_divisores += 1
#     return quantidade_divisores


# maior_numero = 0
# quantidade_div = 0

# m = int(input())

# for j in range(m):
#     if contagem_divisores(j) > quantidade_div:
#         quantidade_div = contagem_divisores(j)
#         maior_numero = j

# print(maior_numero, quantidade_div)


# n = input()

# for i in range(len(n)):
#     for j in range(i+1, len(n)):
#         if n[i] == n[j]:
#             print(i, j)
#             print('iguais')

# def contagem_divisores(n):
#     quantidade_divisores = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             quantidade_divisores += 1
#     return quantidade_divisores


# maior_numero = 0
# quantidade_div = 0

# m = int(input())

# for j in range(m):
#     if contagem_divisores(j) > quantidade_div:
#         quantidade_div = contagem_divisores(j)
#         maior_numero = j

# print(maior_numero, quantidade_div)
