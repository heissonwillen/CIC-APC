/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			13/05/2019

Descrição:		Calcula o valor decimal de um conjunto de bits conforme o padrão IEEE 754
*/

#include <stdio.h>
#include <math.h>

float IEEE754_32(){
	int bit;
	int sinal = 1;
	int aux_expoente = 7;
	int expoente = 0;
	float mantissa = 0;

	int indice;

	char bit_char;

	for (indice = 0; indice < 31; indice++){
		bit_char = getchar();

		if (bit_char == '0'){
			bit = 0;
		} else if (bit_char == '1'){
			bit = 1;
		}

		if (indice == 0)
			if (bit == 1)
				sinal = -1;	
		
		if ((indice > 0) && (indice < 8)){
			expoente += bit * pow(2, aux_expoente);
			aux_expoente--;

			if (indice == 7){
				expoente -= 127;

				aux_expoente = expoente;
				mantissa +=  pow(2, aux_expoente);
			}
		}

		if (indice >= 8){
			mantissa += bit * pow(2, aux_expoente);
			aux_expoente--;
		}
	}

	return mantissa *= sinal;
}

int main(){
	printf("Digite 32 bits: ");
	printf("%f\n", IEEE754_32());

	return 0;
}