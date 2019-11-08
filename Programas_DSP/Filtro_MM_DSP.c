#include <stdio.h>

void Filter_MM(FILE *Data_in, FILE *Data_out, int Mean){

    short Read;
    int Num_Amostra, i, k = 0, Insert = 0, Filter[Mean], Pos = Mean;

    for(i = 0; i < Mean; i++){

        Filter[i] = 0;
    }

    do{

        Num_Amostra = fread(&Read, sizeof(short), 1, Data_in);
        Filter[0] = Read;

        for(i = 0; i < Mean; i++){

            if((Pos - i) >= 0){

                Insert += Filter[Pos - i];
            }

            Pos--;
        }

        for(i = Mean - 1; i > 0; i--){

            Filter[i] = Filter[i - 1];
        }

        Insert = Insert / Mean;
        fwrite(&Insert, sizeof(short), 1, Data_out);
        Insert = 0;
        Pos = Mean;
        k++;
    }while (Num_Amostra);
}

int main(){

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("Sweep_100_3k4.pcm", "rb")) == NULL){

        printf("\nO arquivo de entrada n�o abriu");
        return 0;
    }

    if((Data_out = fopen("Sweep_100_3k4_FilterMM.pcm", "wb")) == NULL){

        printf("\nO arquivo de saida nao abriu");
        return 0;
    }

    Filter_MM(Data_in, Data_out, 32);

    fclose(Data_in);
    fclose(Data_out);

    return 0;
}
