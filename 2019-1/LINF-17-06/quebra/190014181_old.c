/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			17/06/2019

Descrição:		Resolução da questão 2 da Olimpíada Brasileira de Informática – OBI2015
*/

#include <stdio.h>

typedef struct {
	int e, d;
	char c;
} peca_t;

void le_pecas(peca_t* vetor_pecas, const int N){
	int i;

	for (i = 0; i < N; i++)	
		scanf("%d %c %d", &vetor_pecas[i].e, &vetor_pecas[i].c, &vetor_pecas[i].d);
}

void mostra_palavra(peca_t* vetor_pecas, const int N){
	int i, j, aux = 0;

	int num_iteracoes = 0;

	for (i = 0; i < N; i++){
		for (j = 0; j < N; j++){
			num_iteracoes++;
			if (vetor_pecas[j].e == aux){
				printf("%c", vetor_pecas[j].c);
				aux = vetor_pecas[j].d;
			}
		}
	}
	printf("\n\nnum_iteracoes: %d\n", num_iteracoes);
}

int main(){
	const int TAM = 100000;
	int n;
	peca_t vetor_pecas[TAM];

	scanf("%d", &n);
	le_pecas(vetor_pecas, n);
	mostra_palavra(vetor_pecas, n);
	
	return 0;
}