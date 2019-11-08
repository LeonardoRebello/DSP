#include <stdio.h>
#include <stdlib.h>

void Media_Movel(int Mean, FILE *Data_in, FILE *Data_out){

    int Data_filter = 0, N_amost, pos = 0; 
    float Aux[Mean];
    short Input;

    for(int i = 0; i < Mean; i++){

        Aux[i] = 0;
    }

    do{

        N_amost = fread(&Input, sizeof(short), 1, Data_in);

        for(int i = Mean - 1; i > 0; i--){

            Aux[i] = Aux[i-1];
        }

        Aux[0] = Input;

        int swap = Mean;

        for(int i = 0; i < Mean; i++){

            if ((pos - i) >= 0){
                Data_filter += Aux[swap - i];
            }

            swap--;
        }

        Data_filter = Data_filter / Mean;
        fwrite(&Data_filter, sizeof(short), 1, Data_out);
        Data_filter = 0;

        pos++;
    }while (N_amost);
}

int main()
{

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("C:\\Users\\Leonardo\\Desktop\\DSP\\Sweep_100_3k4.pcm", "rb")) == NULL){

        printf("\nErro: Nao abriu o arquivo de entrada");
        return 0;
    }

    if((Data_out = fopen("Sweep_100_3k4_filter.pcm", "wb")) == NULL){

        printf("\nErro: Nao abriu o arquivo de saida");
        return 0;
    }

    Media_Movel(32  , Data_in, Data_out);

    fclose(Data_in);
    fclose(Data_out);

    return 0;
}
