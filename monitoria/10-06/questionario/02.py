def soma_harmonica(x):
    if x == 1:
        return 1
    return 1/x + soma_harmonica(x-1)

# print(soma_harmonica(6))
