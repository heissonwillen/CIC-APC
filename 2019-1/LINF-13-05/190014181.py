def IEEE754_32():
	sinal = 1
	expoente = 0
	aux_expoente = 7
	mantissa = 0

	for indice in range (31):
		bit = int(input())

		if (indice == 0):
			if (bit == 1):
				sinal = -1	
		
		if ((indice > 0) and (indice < 8)):
			expoente += bit * pow(2, aux_expoente)
			aux_expoente -= 1

			if (indice == 7):
				expoente -= 127

				aux_expoente = expoente
				mantissa +=  2 ** aux_expoente

		if (indice >= 8):
			mantissa += bit * 2 ** aux_expoente
			aux_expoente -= 1
		
	return float(mantissa * sinal)


print("Digite 32 bits: ")
print(IEEE754_32())