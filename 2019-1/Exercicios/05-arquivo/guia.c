#include <stdio.h>
#include <stdlib.h>

typedef char string[50];

int cria(char* arquivo) {
  const string str = "Algoritmos e Programação de Computadores";
  const double d = 12.23;
  const int i = 101;

  FILE *fp = fopen(arquivo, "wb+");

  if((fp == NULL) && (!fp) && (fp == 0)) {
      printf("Não foi possível abrir \"%s\".\n", arquivo);
      return EXIT_FAILURE;
  }

  fwrite(str, sizeof(str), 1, fp);
  fwrite(&d, sizeof(d), 1, fp);
  fwrite(&i, sizeof(i), 1, fp);

  fclose(fp);

  return EXIT_SUCCESS;
}

void mostra(char* arquivo) {
  string str;
  double d;
  int i;
  FILE *fp = fopen(arquivo, "rb");

  if(!fp)
      return;

  fread(str, sizeof(str), 1, fp); 
  fread(&d, sizeof(d), 1, fp);
  fread(&i, sizeof(i), 1, fp);
  fclose(fp);

  printf("string = %s\n", str);
  printf("double = %lf\n", d);
  printf("   int = %d\n", i);
}

int main() {
  char arquivo[] = "mencoes.bin";

  if(cria(arquivo) == EXIT_SUCCESS) {
    printf("Leitura correta:\n");
    mostra(arquivo);
  }

  return EXIT_SUCCESS;
}