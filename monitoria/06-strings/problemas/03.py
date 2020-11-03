def sequencia(s):
	if '1' not in s:
		return 0
	new = list(s[s[::-1].index('1'):len(s)-s.index('1')])
	return len(new)-sum(map(int, new))

n = int(input())
for _ in range(n):
	print(sequencia(input()))