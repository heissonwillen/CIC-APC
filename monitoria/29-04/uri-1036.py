from math import sqrt

a, b, c = [float(x) for x in input().split()]

d = b**2 -4*a*c

if d < 0 or a == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(-b+sqrt(d))/(2*a):.5f}')
    print(f'R2 = {(-b-sqrt(d))/(2*a):.5f}')
