#include <stdio.h>

#define Coef 100

int main() {

    FILE *Data_Far, *Data_Near, *Data_Out;

    if((Data_Far = fopen("far.pcm", "rb")) == NULL){

        printf("\nO arquivo far n?o abriu");
        return 0;
    }

    if((Data_Near = fopen("near.pcm", "rb")) == NULL){

        printf("\nO arquivo near nao abriu");
        return 0;
    }

    if((Data_Out = fopen("LEC_Out.pcm", "wb")) == NULL){

        printf("\nO arquivo de saida nao abriu");
        return 0;
    }

    int i;
    short u = 6;

    short Data_OP[Coef] = {0x0};
    short Filter_Adaptive[Coef] = {0x0};
    short Read_Far, Read_Near, error_out, Fir_Out;

    for(i = 0; i < Coef; i++){

        Data_OP[i] = 0;
        Filter_Adaptive[i] = 0;
    }

    while (fread(&Read_Far, sizeof(short), 1, Data_Far) == 1) {
        
        
        Data_OP[0] = Read_Far;
        Fir_Out = 0;

        for (i = 0; i <Coef; i++) {
            Fir_Out += Data_OP[i] * Filter_Adaptive[i];
        }

        fread(&Read_Near, sizeof(short), 1, Data_Near);

        error_out = Read_Near - Fir_Out;

        fwrite(&error_out, sizeof(short), 1, Data_Out);

        for (i = 0; i < Coef; i++) {
            Filter_Adaptive[i] += u * error_out * Data_OP[i];
        }

        for (i = Coef - 1; i > 0; i--) {
            Data_OP[i] = Data_OP[i - 1];
        }
    }

    fclose(Data_Far);
    fclose(Data_Near);
    fclose(Data_Out);

    return 0;
}
