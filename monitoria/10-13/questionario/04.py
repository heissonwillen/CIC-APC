soma_x, soma_y, soma_z = 0, 0, 0
n = int(input())

for i in range(n):
    x, y, z = [int(j) for j in input().split()]

    soma_x += x
    soma_y += y
    soma_z += z

print('YES' if (soma_x==0 and soma_y==0 and soma_z==0) else 'NO')
