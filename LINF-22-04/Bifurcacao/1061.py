dia_inicio = input([])
dia_inicio = int(dia_inicio[4:])

hora_inicio, min_inicio, seg_inicio = int(input().split(" : "))
hora_inicio, min_inicio, seg_inicio = int(hora_inicio), int(min_inicio), int(seg_inicio)

dia_fim = input()
dia_fim = int(dia_fim[4:])

hora_fim, min_fim, seg_fim = input().split(" : ")
hora_fim, min_fim, seg_fim = int(hora_fim), int(min_fim), int(seg_fim)

duracao_dia = 	dia_fim - dia_inicio
duracao_hora = 	hora_fim - hora_inicio
duracao_min = 	min_fim - min_inicio
duracao_seg =	seg_fim - seg_inicio

if duracao_seg < 0:
	duracao_seg += 60
	duracao_min -= 1

if duracao_min < 0:
	duracao_min += 60
	duracao_hora -= 1

if duracao_hora < 0:
	duracao_hora += 24
	if duracao_dia > 0:
		duracao_dia -= 1

print("{} dia(s)".format(duracao_dia))
print("{} hora(s)".format(duracao_hora))
print("{} minuto(s)".format(duracao_min))
print("{} segundo(s)".format(duracao_seg))