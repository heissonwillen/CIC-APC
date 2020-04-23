def f(r, n, i):
    return (r ** i) - n

def df(r, n, i):
    return i * (r ** (i - 1))

def valor_inicial(n):
    return n / 2

def aproxima(r, n, i):
    debug = True
    if (debug):
        print("f({}) = {}".format(r, f(r, n, i)))
        print("f'({}) = {}\n".format(r, df(r, n, i)))
        #print("f({})/f'({}) = {}\n\n".format(r, r, (f(r, n, i)/ (df(r, n, i)))))

    return r - (f(r, n, i) / df(r, n, i))

def erro(r, n, i):
    return abs(r ** i - n)

def Newton_Raphson(n, precisao, i):
    r = valor_inicial(n)
    iteracao = 0

    while erro(r, n, i) >= precisao:
        iteracao += 1
        print("Iteração: {}".format(iteracao))

        r = aproxima(r, n, i)

    return r

def ler_valores():
    n = float(input("Digite N: "))
    i = int(input("Digite o índice da raiz: "))
    precisao = float(input("Digite a precisão: "))

    r = Newton_Raphson(n, precisao, i)

    print("aproximação da raiz: {}".format(r))

while True:
    ler_valores()