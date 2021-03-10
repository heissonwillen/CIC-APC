def soma_ate(n):
    return n*(n+1)/2

a, b = map(int, input().split())

print(int(soma_ate(b)-soma_ate(a-1)))
