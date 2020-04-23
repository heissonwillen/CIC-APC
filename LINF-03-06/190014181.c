/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			06/03/2019

Descrição:		Lê um número inteiro do usuário e indica se este é um palíndromo ou não.
*/

#include <stdio.h>

int eh_palindromo(char* vetor, int tamanho){
	int i = 0;
	int j = tamanho- 1;

	for (i = 0; i < tamanho / 2; i++){
		if (vetor[i] != vetor[j])
			return 0;
		j--;
	}

	return 1;
}

int preenche_vetor(char* vetor){
	char c;
	int i = 0;

	while (1) {
		c = getchar();
		if (c == '\n')
			return i;
  		vetor[i] = c;
		i++;
	}
	return i;
}

int main() {

	const int TAM = 100;
	char vetor[TAM];
	int tamanho = preenche_vetor(vetor);

	if (eh_palindromo(vetor, tamanho))
		printf("É um número palíndromo.\n");
	else
		printf("Não é um número palíndromo.\n");

    return 0;
}