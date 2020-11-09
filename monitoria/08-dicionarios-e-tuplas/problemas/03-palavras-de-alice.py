dicionario = {}

with open('03-livro.txt', 'r') as arquivo_livro:
    palavras = arquivo_livro.read().split()

for palavra in palavras:
    if palavra.lower() in dicionario:
        dicionario[palavra.lower()] += 1
    else:
        dicionario[palavra.lower()] = 1

# for palavra in sorted(dicionario):
#     if palavra.isalpha():
#         arquivo_saida.write(f'{palavra} {dicionario[palavra]}\n')

with open('02-saida.txt', 'w') as arquivo_saida:
    for palavra in sorted(dicionario):
        if palavra.isalpha():
            arquivo_saida.write(f'{palavra} {dicionario[palavra]}\n')
