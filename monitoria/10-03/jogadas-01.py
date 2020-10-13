import time

def jogadas(a, b):
    diff = abs(a-b)
    print(diff//10 if diff%10==0 else diff//10+1)

inicio = time.time()
jogadas(123456789, 1000000000)
fim = time.time()
print(fim - inicio, 'segundos')
