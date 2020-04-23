#include <stdio.h>

void mostra_dobro(int* vetor, const int N){
	int i;

	for (i = 0; i < N; i++)
		printf("%d ", 2 * vetor[i]);

	printf("\n");
}

void mostra_modulo(int* vetor, const int N){
	int i;

	for (i = 0; i < N; i++)
		if (vetor[i] < 0)
			printf("%d ", -1 * vetor[i]);
		else
			printf("%d ", vetor[i]);

	printf("\n");
}

int main(){
	const int N = 10;

	int vetor[N], i;

	for (i = 0; i < N; i++)
		scanf("%d", &vetor[i]);

	mostra_dobro(vetor, N);
	mostra_modulo(vetor, N);

	return 0;
}