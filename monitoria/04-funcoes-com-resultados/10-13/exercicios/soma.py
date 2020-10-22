# Realiza a soma de n valores dados pelo usuário
# O número de iterações é dado pelo usuário

n = int(input())

soma = 0

# for i in range(n):
#     soma += int(input())
#
# print(soma)

while n > 0:
    soma += int(input())
    n -= 1

print(soma)
