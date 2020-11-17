with open('notas_estudantes.dat', 'r') as arquivo_notas:
	s = arquivo_notas.readlines()
	linhas = [linha.split() for linha in s]

	for linha in linhas:
		if len(linha) > 7:
			print(linha[0])