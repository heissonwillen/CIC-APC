import time

def jogadas(a, b):
    k = 10
    count = 0

    if b > a:
        a, b = b, a

    while(b < a):
        b += k
        count += 1
    print(count)

inicio = time.time()

jogadas(123456789, 1000000000)

fim = time.time()
print(fim - inicio, 'segundos')
