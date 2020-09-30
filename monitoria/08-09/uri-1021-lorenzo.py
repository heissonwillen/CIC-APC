dinheiro = float(input())


#NOTAS
nota100 = dinheiro // 100
resto = dinheiro % 100
nota100 = "{:.0f}".format(nota100)
nota50 = resto // 50
resto = resto % 50
nota50 = "{:.0f}".format(nota50)
nota20 = resto // 20
resto = resto % 20
nota20 = "{:.0f}".format(nota20)
nota10 = resto // 10
resto = resto % 10
nota10 = "{:.0f}".format(nota10)
nota5 = resto // 5
resto = resto % 5
nota5 = "{:.0f}".format(nota5)
nota2 = resto // 2
resto = resto % 2
nota2 = "{:.0f}".format(nota2)


#MOEDAS
moeda01 = resto // 1
resto = resto % 1
moeda01 = "{:.0f}".format(moeda01)
moeda50 = resto // (1/2)
resto = resto % (1/2)
moeda50 = "{:.0f}".format(moeda50)
moeda25 = resto // (1/4)
resto = resto % (1/4)
moeda25 = "{:.0f}".format(moeda25)
moeda10 = resto // (1/10)
resto = resto % (1/10)
moeda10 = "{:.0f}".format(moeda10)
moeda5 = resto // (1/20)
resto = resto % (1/20)
moeda5 = "{:.0f}".format(moeda5)
moeda1 = resto // (1/100)
resto = resto % (1/100)
moeda1 = "{:.0f}".format(moeda1)


print("NOTAS:")
print(nota100 + " nota(s) de R$ 100.00")
print(nota50 + " nota(s) de R$ 50.00")
print(nota20 + " nota(s) de R$ 20.00")
print(nota10 + " nota(s) de R$ 10.00")
print(nota5 + " nota(s) de R$ 5.00")
print(nota2 + " nota(s) de R$ 2.00")
print("MOEDAS:")
print(moeda01 + " moeda(s) de R$ 1.00")
print(moeda50 + " moeda(s) de R$ 0.50")
print(moeda25 + " moeda(s) de R$ 0.25")
print(moeda10 + " moeda(s) de R$ 0.10")
print(moeda5 + " moeda(s) de R$ 0.05")
print(moeda1 + " moeda(s) de R$ 0.01")
