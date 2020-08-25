dia = int(input())

ano = int(dia / 365)
dia %= 365

mes = int(dia / 30)
dia %= 30

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))