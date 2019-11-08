#include <stdio.h>

int main(){

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("Sweep_100_3k4.pcm", "rb")) == NULL){

        printf("\nO arquivo de entrada n�o abriu");
        return 0;
    }

    if((Data_out = fopen("Sweep_100_3k4_Identificador.pcm", "wb")) == NULL){

        printf("\nO arquivo de saida nao abriu");
        return 0;
    }

    fseek(Data_in, 0L, SEEK_END);
    int len = (ftell(Data_in) / sizeof(short));
    rewind(Data_in);

    short Filter_Length = 4, i, j, Num_Amostras;
    short Read, Data_Op[Filter_Length], Erro;
    short Filter_Unknown[] = {8192, 8192, 8192, 8192}, Filter_Adaptive[Filter_Length], Value_Adaptive, Value_Unknown;
    short u = 6;

    for(i = 0; i < Filter_Length; i++){

        Data_Op[i] = 0;
        Filter_Adaptive[i] = 0;
    }

    for(i = 0; i < len; i++){

        Num_Amostras = fread(&Read, sizeof(short), 1, Data_in);
        Data_Op[0] = Read;

        Value_Adaptive = 0;
        Value_Unknown = 0;

        for(j = 0; j < Filter_Length; j++){

            Value_Adaptive = Value_Adaptive + Data_Op[j] * (Filter_Adaptive[j]);
            Value_Unknown = Value_Unknown + Data_Op[j] * (Filter_Unknown[j]);
        }

        Erro = (short)Value_Unknown - (short)Value_Adaptive;
        fwrite(&Erro, sizeof(short), 1, Data_out);

        for(j = 0; j < Filter_Length; j++){

            Filter_Adaptive[j] = Filter_Adaptive[j] + (u * Erro * Data_Op[j]);
        }

        for(j = Filter_Length-1; j > 0; j--){

            Data_Op[j] = Data_Op[j - 1];
        }
    }

    fclose(Data_in);
    fclose(Data_out);

    return 0;
}
