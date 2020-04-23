'''
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			27/05/2019

Descrição:		Prática com o uso de vetores.
'''

def le_tamanho_do_vetor():
	n = -1
	while (n < 1 or n > 100):
		n = int(input('Digite N: '))
	return n

def uma_letra():
	while True:
		c = input('')
		if ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
			return c[0]
		else:
			print('Letra inválida. ', end = '')

def le_elementos(vetor, N):
	for i in range (N):
		vetor[i] = uma_letra()

def mostra(vetor, N):
	for i in range (N):
		print(vetor[i], end = '')

def ordena(vetor, N):
	for i in range (N):
		for j in range (N):
			if (j < N - 1):
				if (vetor[j] > vetor[j + 1]):
					vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def indice_de(vetor, N, c):
	for i in range (N):
		if (vetor[i] == c):
			return i
	return -1

def busca_letra(vetor, N):
	c = uma_letra()
	i = indice_de(vetor, N, c)

	if (i >= 0):
		print('\nO caractere \'{}\' está na {}a posição do vetor.'.format(c, i))
	else:
		print('O caractere \'{}\' não está no vetor.'.format(c))

def main():
	vetor = [' '] * 100
	N = le_tamanho_do_vetor()

	le_elementos(vetor, N)
	print('\nO vetor é: ')
	mostra(vetor, N)
	busca_letra(vetor, N)

	ordena(vetor, N)
	print("\nO vetor ordenado é: ")
	mostra(vetor, N)
	busca_letra(vetor, N)

main()