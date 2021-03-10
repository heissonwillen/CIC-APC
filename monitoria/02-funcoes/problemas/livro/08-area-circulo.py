import math

def quadrado(n):
    return n * n

def area_circulo(r):
    area = math.pi * quadrado(r)
    return area

print(area_circulo(1))
print(area_circulo(3))