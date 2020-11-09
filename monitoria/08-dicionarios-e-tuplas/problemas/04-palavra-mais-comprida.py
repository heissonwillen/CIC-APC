'''
https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html
'''

dicionario = {}

with open('03-livro.txt', 'r') as arquivo_livro:
    palavras = arquivo_livro.read().split()

for palavra in palavras:
    if palavra.isalpha():
        dicionario[len(palavra)] = palavra

# print(sorted(dicionario, reverse=True))
chave_maior_palavra = sorted(dicionario, reverse=True)[0]
print(chave_maior_palavra)
print(dicionario[chave_maior_palavra])
