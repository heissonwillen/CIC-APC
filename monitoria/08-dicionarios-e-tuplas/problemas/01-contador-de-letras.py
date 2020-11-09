'''
https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html
'''

string = input().lower()
tabela = dict()

# for caractere in string:
#     if caractere.isalpha():
#         if caractere not in tabela:
#             tabela[caractere] = 1
#         else:
#             tabela[caractere] += 1

for caractere in string:
    if caractere.isalpha():
        tabela[caractere] = 1 if caractere not in tabela else tabela[caractere] + 1

for chave in sorted(tabela):
    print(chave, tabela[chave])
