def f(r, n):
    return (r * r) - n

def fp(r, n):
    return 2 * r

def valor_inicial(n):
    return n / 2

def aproxima(r, n):
    return r - f(r, n) / fp(r, n)

def erro(r, n):
    return abs(r * r - n)

def Newton_Raphson(n, iteracoes, precisao):
    r = valor_inicial(n)

    for i in range(iteracoes):
        r = aproxima(r, n)

        if precisao >= erro(r, n):
            break
    return r

def ler_valores():
    n = float(input("Digite N: "))
    iteracoes = int(input("Digite o número máximo de iterações: "))
    precisao = float(input("Digite o erro mínimo: "))

    r = Newton_Raphson(n, iteracoes, precisao)

    print("aproximação da raiz: {}".format(r))

while True:
    ler_valores()