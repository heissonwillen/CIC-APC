hora_inicio, min_inicio, hora_fim, min_fim = input().split()
hora_inicio, min_inicio, hora_fim, min_fim = int(hora_inicio), int(min_inicio), int(hora_fim), int(min_fim)

duracao_horas = 24 - hora_inicio + hora_fim
duracao_min = 60 - min_inicio + min_fim


if duracao_horas > 24:
	duracao_horas -= 24

if min_inicio > min_fim:
	duracao_horas -= 1

if min_fim > min_inicio and hora_fim == hora_inicio:
	duracao_horas = 0

if duracao_horas == 24:
	duracao_min = 0

if duracao_min > 60:
	duracao_min -= 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas, duracao_min))