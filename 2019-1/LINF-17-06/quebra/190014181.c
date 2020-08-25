/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			17/06/2019

Descrição:		Resolução da questão 2 da Olimpíada Brasileira de Informática – OBI2015
*/

#include <stdio.h>

#define TAM 200000

typedef struct {
	int d;
	char c;
} peca_t;

void le_pecas(peca_t* pecas, const int N){
	int i, e;

	for (i = 0; i < N; i++){
		scanf("%d ", &e);
		scanf("%c %d", &pecas[e].c, &pecas[e].d);
	}
}

void mostra(peca_t* pecas){
	int i = 0;

	while (i != 1){
		putchar(pecas[i].c);
		i = pecas[i].d;
	}

	putchar('\n');
}

int main(){
	int n;
	peca_t pecas[TAM];

	scanf("%d", &n);
	le_pecas(pecas, n);
	mostra(pecas);
	
	return 0;
}