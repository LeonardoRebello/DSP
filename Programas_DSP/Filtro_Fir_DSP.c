/* Implementa??o de um filtro FIR 
L? um arquivo bin?rio com amostras em 16bits
Salva arquivo filtrado tamb?m em 16 bits
Walter vers?o 1.0 
 */
#include <stdio.h>
#include <cycles.h>

#define NSAMPLES 58

int main()
{
  cycle_stats_t stats;
  
  FILE *in_file, *out_file;
  int i, n, n_amost;

  short entrada, saida;
  short sample[NSAMPLES] = {0x0};

  short y = 0;

  //filtro passa-baixas fc=200Hz

  short coef[NSAMPLES] = {-180, -65, -278, -373, -271, -26, 271, 543, 707, 711, 537, 249, -26, -154, -62, 206, 501, 596, 314, -399, -1418, -2431, -3057, -2955, -1998, -324, 1667, 3443, 4482, 4482, 3443, 1667, -324, -1998, -2955, -3057, -2431, -1418, -399, 314, 596, 501, 206, -62, -154, -26, 249, 537, 711, 707, 543, 271, -26, -271, -373, -278, -65, -180};

  
  /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("Sweep_100_3k4.pcm", "rb")) == NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("..//sai_sweep.pcm", "wb")) == NULL)
  {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

  // zera vetor de amostras
  for (i = 0; i < NSAMPLES; i++)
  {
    sample[i] = 0;
  }

  // execu??o do filtro
  CYCLES_INIT(stats);
  do
  {

    //zera sa?da do filtro
    y = 0;

    //l? dado do arquivo
    n_amost = fread(&entrada, sizeof(short), 1, in_file);
    sample[0] = entrada;

    //Convolu??o e acumula??o
    CYCLES_START(stats);
    for (n = 0; n < NSAMPLES; n++)
    {
      y += coef[n] * sample[n];
    }

    //desloca amostra
    for (n = NSAMPLES - 1; n > 0; n--)
    {
      sample[n] = sample[n - 1];
    }
    CYCLES_STOP(stats);

    saida = y;

    //escreve no arquivo de sa?da
    fwrite(&saida, sizeof(short), 1, out_file);

  } while (n_amost);

  //fecha os arquivos de entrada de sa?da
  fclose(out_file);
  fclose(in_file);
  CYCLES_PRINT(stats);
  return 0;
}
