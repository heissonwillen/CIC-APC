val = int(input())

n = val

nota100 = int(n / 100)
n %= 100

nota50 = int(n / 50)
n %= 50

nota20 = int(n / 20)
n %= 20

nota10 = int(n / 10)
n %= 10

nota05 = int(n / 5)
n %= 5

nota02 = int(n / 2)
n %= 2

nota01 = n

print(val)
print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota05))
print("{} nota(s) de R$ 2,00".format(nota02))
print("{} nota(s) de R$ 1,00".format(nota01))
