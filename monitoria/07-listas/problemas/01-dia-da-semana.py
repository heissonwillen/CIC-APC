'''
Dado um numero de 1 a 7 (esses inclusos), mostrar, na saída padrão o dia da semana correspondente a esse número.

Exemplos:
1
>>> 'Domingo'
5
>>> 'Quinta'
'''

# dia = int(input())
#
# if dia == 1:
#     print('Domingo')
# elif dia == 2:
#     print('Segunda')
# elif dia == 3:
#     print('Terca')
# elif dia == 4:
#     print('Quarta')
# elif dia == 5:
#     print('Quinta')
# elif dia == 6:
#     print('Sexta')
# elif dia == 7:
#     print('Sabado')

dias_da_semana = ['', 'Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
dia = int(input())

print(dias_da_semana[dia])
