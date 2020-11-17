with open('notas_estudantes.dat', 'r') as arquivo_notas:
    s = arquivo_notas.readlines()
    linhas = [linha.split() for linha in s]

    for linha in linhas:
        nome = linha[0]
        notas = list(map(int, linha[1:]))
        media = sum(notas)/len(notas)
        print(nome, media)
