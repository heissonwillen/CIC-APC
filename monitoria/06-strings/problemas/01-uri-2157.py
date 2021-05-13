'''
3
1 5
10 13
98 101
'''


n = int(input())

for i in range(n):
    a, b = [int(j) for j in input().split()]

    k = ''

    for i in range(a, b+1):
        k += str(i)

    print(k + k[::-1])
