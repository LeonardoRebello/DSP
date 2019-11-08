#include <stdio.h>
#include <stdlib.h>

#define nAmostrasArq    10400
#define Threshold        8000
#define ContadorPausa     200

void convolveShort(double Signal[/* SignalLen */], size_t SignalLen,
                   short Kernel[/* KernelLen */], size_t KernelLen,
                   double Result[/* SignalLen + KernelLen - 1 */])
{
    size_t n;

    for (n = 0; n < SignalLen + KernelLen - 1; n++)
    {
        size_t kmin, kmax, k;

        Result[n] = 0;

        kmin = (n >= KernelLen - 1) ? n - (KernelLen - 1) : 0;
        kmax = (n < SignalLen - 1) ? n : SignalLen - 1;

        for (k = kmin; k <= kmax; k++)
        {
            Result[n] += Signal[k] * Kernel[n - k];
        }
    }
}

size_t read_coefs(double** vector,char* fileName){
    FILE *arq;
    size_t  tam;

    arq=fopen(fileName,"rb");               //abre arquivo de entrada

    fseek(arq, 0, SEEK_END);                //vai pro final do arquivo
    tam = ftell(arq)/sizeof(double);        //pega o tamanho do arquivo
    rewind(arq);                            //move para o inicio

    //*vector = (double*) malloc(tam*sizeof(double)); //aloca vetor
    *vector = (double*) calloc(tam,sizeof(double));

    fread(*vector, sizeof(double), tam, arq); //le para o vetor

    fclose(arq);                            //fecha o arquivo de entrada

    return tam;
}

size_t read_input(short** vector,char* fileName){
    FILE *arq;
    size_t  tam;

    arq=fopen(fileName,"rb");               //abre arquivo de entrada

    fseek(arq, 0, SEEK_END);                //vai pro final do arquivo
    tam = ftell(arq)/sizeof(short);        //pega o tamanho do arquivo
    rewind(arq);                            //move para o inicio

    *vector = (short*) malloc(tam*sizeof(short)); //aloca vetor

    fread(*vector, sizeof(short), tam, arq); //le para o vetor

    fclose(arq);                            //fecha o arquivo de entrada

    return tam;
}

int main() {
    double *coef697, *coef770, *coef852, *coef941, *coef1209, *coef1336, *coef1477;
    size_t n697, n770, n852, n941, n1209, n1336, n1477;
    short *entrada;

    read_input(&entrada, "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\DTMF\\DTMF2R.pcm");

    n697 = read_coefs(&coef697,
                      "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef697.pcm");
    double saida697[nAmostrasArq+n697-1];
    convolveShort(coef697,n697,entrada,nAmostrasArq,saida697);

    n770 = read_coefs(&coef770,
                      "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef770.pcm");
    double saida770[nAmostrasArq+n770-1];
    convolveShort(coef770,n770,entrada,nAmostrasArq,saida770);

    n852 = read_coefs(&coef852,
                      "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef852.pcm");
    double saida852[nAmostrasArq+n852-1];
    convolveShort(coef852,n852,entrada,nAmostrasArq,saida852);

    n941 = read_coefs(&coef941,
                      "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef941.pcm");
    double saida941[nAmostrasArq+n941-1];
    convolveShort(coef941,n941,entrada,nAmostrasArq,saida941);

    n1209 = read_coefs(&coef1209,
                       "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef1209.pcm");
    double saida1209[nAmostrasArq+n1209-1];
    convolveShort(coef1209,n1209,entrada,nAmostrasArq,saida1209);

    n1336 = read_coefs(&coef1336,
                       "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef1336.pcm");
    double saida1336[nAmostrasArq+n1336-1];
    convolveShort(coef1336,n1336,entrada,nAmostrasArq,saida1336);

    n1477 = read_coefs(&coef1477,
                       "C:\\Users\\BTW_A\\GitHub\\Faculdade\\2017_2\\DSP\\CodigosC\\FIR_BP\\cmake-build-debug\\FIRBPcoef1477.pcm");
    double saida1477[nAmostrasArq+n1477-1];
    convolveShort(coef1477,n1477,entrada,nAmostrasArq,saida1477);


    char telefone[10];
    int i, pos=0, contador=-1, coluna=0, linha=0, tam;

    for(i=0;i<(nAmostrasArq+n697-1);i++)
    {
        if(contador!=-1)
            contador-=1;
        if(abs(saida697[i])>Threshold){
            linha=1;
            contador=ContadorPausa;
        }
        else if(abs(saida770[i])>Threshold){
            linha=2;
            contador=ContadorPausa;
        }
        else if(abs(saida852[i])>Threshold){
            linha=3;
            contador=ContadorPausa;
        }
        else if(abs(saida941[i])>Threshold){
            linha=4;
            contador=ContadorPausa;
        }
        if(abs(saida1209[i])>Threshold){
            coluna=1;
            contador=ContadorPausa;
        }
        else if(abs(saida1336[i])>Threshold){
            coluna=2;
            contador=ContadorPausa;
        }
        else if(abs(saida1477[i])>Threshold){
            coluna=3;
            contador=ContadorPausa;
        }
        if(!contador||i+1==tam&&contador!=-1)
        {
            switch(linha)
            {
                case 1:
                    switch(coluna)
                    {
                        case 1:
                            telefone[pos]='1';
                            break;
                        case 2:
                            telefone[pos]='2';
                            break;
                        case 3:
                            telefone[pos]='3';
                            break;
                        default:
                            break;
                    }
                    break;
                case 2:
                    switch(coluna)
                    {
                        case 1:
                            telefone[pos]='4';
                            break;
                        case 2:
                            telefone[pos]='5';
                            break;
                        case 3:
                            telefone[pos]='6';
                            break;
                        default:
                            break;
                    }
                    break;
                case 3:
                    switch(coluna)
                    {
                        case 1:
                            telefone[pos]='7';
                            break;
                        case 2:
                            telefone[pos]='8';
                            break;
                        case 3:
                            telefone[pos]='9';
                            break;
                        default:
                            break;
                    }
                    break;
                case 4:
                    switch(coluna)
                    {
                        case 1:
                            telefone[pos]='*';
                            break;
                        case 2:
                            telefone[pos]='0';
                            break;
                        case 3:
                            telefone[pos]='#';
                            break;
                        default:
                            break;
                    }
                    break;
                default:
                    break;

            }
            pos++;
            linha=0;
            coluna=0;
        }
    }
    telefone[pos]='\0';
    puts(telefone);
    return 0;
}