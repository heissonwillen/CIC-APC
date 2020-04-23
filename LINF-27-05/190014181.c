/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			27/05/2019

Descrição:		Prática com o uso de vetores.
*/

#include <stdio.h>

int le_tamanho_do_vetor() {
	int n = -1;

	while (n < 1 || n > 100){
		printf("Digite N: \n");
		scanf("%d", &n);
	}
	return n;
}

char uma_letra() {
	char c;

	while (1){
		c = getchar();

		if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
			return c;
		else if (c != 10)
			printf("Letra inválida.\n");
	}
	return 0;
}

void le_elementos(char *vetor, int N) {
	int i;

	for (i = 0; i < N; i++)
		vetor[i] = uma_letra();
}

void mostra(char *vetor, int N) {
	int i;

	for (i = 0; i < N; i++)
		putchar(vetor[i]);
}

void ordena(char *vetor, int N) {
	int i, j;
	char aux;

	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			if (j < N - 1)
				if (vetor[j] > vetor[j + 1]){
					aux = vetor[j];
					vetor[j] = vetor[j + 1];
					vetor[j + 1] = aux;
				}
}

int indice_de(char *vetor, int N, char c) {
	int i;

	for (i = 0; i < N; i++)
		if (vetor[i] == c)
			return i;

	return -1;
}

void busca_letra(char *vetor, int N) {
	char c = uma_letra();
	int i = indice_de(vetor, N, c);

	if(i >= 0)
		printf("\nO caractere '%c' está na %da posição do vetor.\n", c, i);
	else
		printf("\nO caractere '%c' não está no vetor.\n", c);
}

int main() {	
	char vetor[100];
	int N = le_tamanho_do_vetor();

	le_elementos(vetor, N);
	printf("\nO vetor é: ");
	mostra(vetor, N);
	busca_letra(vetor, N);

	ordena(vetor, N);
	printf("\nO vetor ordenado é: ");
	mostra(vetor, N);
	busca_letra(vetor, N);

    return 0;
}