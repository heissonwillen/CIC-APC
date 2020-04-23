n = int(input())

prev_number = 0;
number = 1
aux = 0

sequencia = str(prev_number) + " " + str(number)

for i in range (0, n - 2):
	aux = prev_number + number
	prev_number = number
	number =  aux 

	sequencia += " " + str(aux)

print(sequencia)