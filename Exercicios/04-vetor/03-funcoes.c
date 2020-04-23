#include <stdio.h>

void mostra_pares(int* vetor, const int N){
	int i;

	for (i = 0; i < N; i++)
		if (vetor[i] % 2 == 0)
			printf("%d ", vetor[i]);

	printf("\n");
}

void mostra_menor_que_2(int* vetor, const int N){
	int i;

	for (i = 0; i < N; i++)
		if (vetor[i] < 2)
			printf("%d ", vetor[i]);

	printf("\n");
}

void mostra_positivo(int* vetor, const int N){
	int i;

	for (i = 0; i < N; i++)
		if (vetor[i] > 0)
			printf("%d ", vetor[i]);

	printf("\n");
}

int main(){
	const int N = 10;

	int vetor[N], i;

	for (i = 0; i < N; i++)
		scanf("%d", &vetor[i]);

	mostra_positivo(vetor, N);
	mostra_menor_que_2(vetor, N);
	mostra_pares(vetor, N);

	return 0;
}