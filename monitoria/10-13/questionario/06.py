n, preco = [int(i) for i in input().split()]

soma = 0
for i in range(n):
    soma += int(input())

media = int(soma/n)
print(f'media: {media}')
print('o rock reinara mais uma vez' if media >= preco else 'rockeiros trabalhando ja')
