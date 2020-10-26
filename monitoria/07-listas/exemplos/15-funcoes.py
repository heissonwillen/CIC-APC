def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - n

def multiplica(a, b):
    return a * b

def divide(a, b):
    return a / b

funcoes = [
    subtrai,
    soma,
    multiplica,
    divide
]

n = int(input())
a, b = [float(x) for x in input().split()]

print(funcoes[n](a, b))
