#include <stdio.h>

int main(){
	const int M = 100, N = M;

	float matriz[M][N], media_linha, media_geral;
	int m, n, i, j;

	scanf("%d", &m);
	scanf("%d", &n);

	for (i = 0; i < m; i++)
		for (j = 0; j < n; j++)
			scanf("%f", &matriz[i][j]);

	printf("\n");
	for (i = 0; i < m; i++){
		for (j = 0; j < n; j++)
			media_linha += matriz[i][j];
		
		media_geral += media_linha;
		media_linha /= j;
		printf("%.2f\n", media_linha);
		media_linha = 0;
	}	
	media_geral /= (i * j);
	printf("%.2f\n", media_geral);

	return 0;
}