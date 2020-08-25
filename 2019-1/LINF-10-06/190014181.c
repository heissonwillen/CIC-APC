/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			10/06/2019

Descrição:		cor
*/

#include <stdio.h>

int numerico(char c){
	if (c >= '0' && c <= '9')
		return 1;
	return 0;
}

void preenche_matriz(int matriz[][100], int dimensao){
	int i, j;
	char c;

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			c = getchar();

			if (numerico(c))
				matriz[i][j] = (c - '0');
			else
				matriz[i][j] = -1;
		}
		getchar();
	}
}

void conta_cores(int matriz[][100], int dimensao){
	int i, j, num_iteracao = 0;

	int aux_i = 0, aux_j = 0;



	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			if (matriz[i][j] != 0){
				/*
				if (matriz[i][j - 1] == num_iteracao || matriz[i][j + 1] == num_iteracao || matriz[i - 1][j] == num_iteracao || matriz[i + 1][j] == num_iteracao){
					matriz[i][j] = num_iteracao + 1;
				}*/
			}


			
		}
	}



}

void mostra_matriz(int matriz[][100], int dimensao){
	int i, j;

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			if (matriz[i][j] >= 0)
				printf("%d", (matriz[i][j]));
			else 
				printf(" ");
		}
		putchar('\n');
	}
}

int main(){

	const int DIMENSAO = 100;
	int dimensao;

	int matriz[DIMENSAO][DIMENSAO];

	scanf("%d", &dimensao);
	getchar();

	preenche_matriz(matriz, dimensao);
	mostra_matriz(matriz, dimensao);

	conta_cores(matriz, dimensao);

	mostra_matriz(matriz, dimensao);

	return 0;
}