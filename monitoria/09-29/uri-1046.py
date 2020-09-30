inicio, fim = [int(x) for x in input().split()]

duracao = 24 - inicio + fim

if duracao > 24:
	duracao -= 24

print(f'O JOGO DUROU {duracao} HORA(S)')
