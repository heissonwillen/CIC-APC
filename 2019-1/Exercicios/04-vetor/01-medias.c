#include <stdio.h>

int main(){
	const int N = 100;

	float notas[N], media = 0;

	int n, i;

	printf("Número de alunos: ");
	scanf("%d", &n);

	for (i = 0; i < n; i++){
		printf("Nota do aluno %d: ", i + 1);
		scanf("%f", &notas[i]);

		media += notas[i];
	}

	media /= i;

	printf("%.2f\n", media);

	for (i = 0; i < n; i++){
		if (notas[i] >= media)
			printf("%.2f\n", notas[i]);
	}

	return 0;
}