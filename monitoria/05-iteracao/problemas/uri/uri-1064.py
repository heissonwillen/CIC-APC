soma = positivos = 0

for _ in range(6):
    n = float(input())
    if n > 0:
        soma += n
        positivos += 1

print(f'{positivos} valores positivos')
print(f'{soma / positivos:.1f}')
