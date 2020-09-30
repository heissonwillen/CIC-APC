# Exemplo de leitura de mais de uma variável em uma única linha

# a, b = (float(x) for x  in input().split())
# a, b = map(float, input().split())

val = (float(x) for x  in input().split())

print(val)

# print(a, b)
