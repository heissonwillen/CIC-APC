#include <stdio.h>

int main(){
	const int N = 1000;

	float sal_funcionarios[N];

	int n, i, num_filhos;

	printf("Digite o número de funcionários: \n");
	scanf("%d", &n);

	for (i = 0; i < n; i++){
		printf("Quantidade de filhos do funcionário %d:\n", i + 1);
		scanf("%f", &num_filhos);
	}



	return 0;
}