n = int(input())

aux = 1

for i in range (n):
	for j in range (0, 3):
		print(aux, end = " ")
		aux += 1
	aux += 1
	print("PUM")