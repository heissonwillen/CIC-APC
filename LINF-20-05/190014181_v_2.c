/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			22/05/2018

Descrição:		Troca cada letra pelo equivalente em X posições.
*/

#include <stdio.h>

void cifra(int x){
	getchar();
	
	while(c != '\n'){
		c = getchar();

		if (((c >= 'A') && (c <= 'Z') && (c + x > 'Z')) || ((c >= 'a') && (c <= 'z') && (c + x > 'z')))
			c -= 26;

		if (c != '\n')
			printf("%c", c + x);
	}
}

void decifra(int x){
	decifra (('a' - 'z') - x);
}

int main(){
	int x = 0;

	printf("Digite o número de posições (cifra): ");
	scanf("%d", &x);

	cifra(x);
	printf("\n");

	printf("Digite o número de posições (decifra): ");
	scanf("%d", &x);
	printf("\n");

	decifra(x);

	printf("\n");

	return 0;
}