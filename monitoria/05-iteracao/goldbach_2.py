import time

def eratosthenes(n):
    primes = list(range(2, n+1))
    for i in primes:
        j = 2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j = j+1
    return primes


def odd_primes(N):
    oddprimes = eratosthenes(N)
    oddprimes.remove(2)
    return(oddprimes)


def goldbach(N):
    x, y = 0, 0
    result = 0
    if N % 2 == 0:
        prime = odd_primes(N)
        while result != N:
            for i in range(len(prime)):
                if result == N:
                    break
                x = prime[i]
                for j in range(len(prime)):
                    y = prime[j]
                    result = x + y
                    if result == N:
                        break
    return x, y


i = time.time()
goldbach(int(1e7))
f = time.time()

print(f-i)
