s = 'sou uma string'

for i in range(len(s)-1, -1, -1):
    print(s[i])

i = len(s)-1
while i >= 0:
    print(s[i])
    i -= 1
