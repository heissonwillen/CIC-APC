# Valores das notas/moedas

nota100 = int(100)
nota50 = int(50)
nota20 = int(20)
nota10 = int(10)
nota5 = int(5)
nota2 = int(2)
moeda01 = int(1)
moeda50 = float(0.50)
moeda25 = float(0.25)
moeda10 = float(0.10)
moeda5 = float(0.05)
moeda1 = float(0.01)

# Função que faz o calculo de quantas notas/moedas são necessarias para formar o valor


def qntd_notas():
    N = float(input())
    # NOTAS
    notade100 = int(N//nota100)
    N = N - notade100*100
    notade50 = int(N//nota50)
    N = N - notade50*50
    notade20 = int(N//nota20)
    N = N - notade20*20
    notade10 = int(N//nota10)
    N = N - notade10*10
    notade5 = int(N//nota5)
    N = N - notade5*5
    notade2 = int(N//nota2)
    N = N - notade2*2

    # MOEDAS
    moedade01 = int((N//moeda01))
    N = float(N - moedade01*1)
    moedade50 = int((N//moeda50))
    N = float(N - moedade50*0.50)
    moedade25 = int((N//moeda25))
    N = float(N - moedade25*0.25)
    moedade10 = int((N//moeda10))
    N = float(N - moedade10*0.10)
    moedade5 = int((N//moeda5))
    N = float(N - moedade5*0.5)
    moedade1 = int((N//moeda1))
    N = float(N - moedade1*0.01)

    print(f"NOTAS:")
    print(f"{notade100} nota(s) de R$ 100.00")
    print(f"{notade50} nota(s) de R$ 50.00")
    print(f"{notade20} nota(s) de R$ 20.00")
    print(f"{notade10} nota(s) de R$ 10.00")
    print(f"{notade5} nota(s) de R$ 5.00")
    print(f"{notade2} nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{moedade01} moeda(s) de R$ 1.00")
    print(f"{moedade50} moeda(s) de R$ 0.50")
    print(f"{moedade25} moeda(s) de R$ 0.25")
    print(f"{moedade10} moeda(s) de R$ 0.10")
    print(f"{moedade5} moeda(s) de R$ 0.05")
    print(f"{moedade1} moeda(s) de R$ 0.01")


qntd_notas()


"""

"""