positivos = 0
for _ in range(6):
    value = float(input())

    if value > 0:
        positivos += 1

print(f'{positivos} valores positivos')
