n = float(input())

moeda001 = (n - int(n)) * 100
nota100 = int(n / 100)
n %= 100
nota050 = int(n / 50)
n %= 50
nota020 = int(n / 20)
n %= 20
nota010 = int(n / 10)
n %= 10
nota005 = int(n / 5)
n %= 5
nota002 = int(n / 2)
n %= 2

moeda100 = int(n)
moeda001 = int(round(moeda001))
moeda001 %= 100
moeda050 = int(moeda001 / 50)
moeda001 %= 50
moeda025 = int(moeda001 / 25)
moeda001 %= 25
moeda010 = int(moeda001 / 10)
moeda001 %= 10
moeda005 = int(moeda001 / 5)
moeda001 %= 5
moeda001 = int(round(moeda001))

print("NOTAS:\n{} nota(s) de R$ 100.00".format(nota100))
print("{} nota(s) de R$ 50.00".format(nota050))
print("{} nota(s) de R$ 20.00".format(nota020))
print("{} nota(s) de R$ 10.00".format(nota010))
print("{} nota(s) de R$ 5.00".format(nota005))
print("{} nota(s) de R$ 2.00".format(nota002))

print("MOEDAS:\n{} moeda(s) de R$ 1.00".format(moeda100))
print("{} moeda(s) de R$ 0.50".format(moeda050))
print("{} moeda(s) de R$ 0.25".format(moeda025))
print("{} moeda(s) de R$ 0.10".format(moeda010))
print("{} moeda(s) de R$ 0.05".format(moeda005))
print("{} moeda(s) de R$ 0.01".format(moeda001))
