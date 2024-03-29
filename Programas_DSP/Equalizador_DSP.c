#include <stdio.h>

int main()
{

    FILE *Data_in, *Data_out;

    if((Data_in = fopen("Sweep_100_3k4.pcm", "rb")) == NULL)
    {

        printf("\nErro: Nao abriu o arquivo de entrada");
        return 0;
    }

    if((Data_out = fopen("Equa.pcm", "wb")) == NULL)
    {

        printf("\nErro: Nao abriu o arquivo de saida");
        return 0;
    } 

    short Num_Amostras = 192, i;

    float LOWPASS[] = {0, -2, -5, -7, -9, -9, -9, -8, -5, -2, 1, 5, 10, 13, 16, 16, 16, 13, 8, 1, -6, -14, -21, -27, -31, -31, -28, -20, -10, 2, 17, 31, 43, 52, 56, 53, 44, 29, 9, -14, -39, -62, -80, -91, -93, -84, -64, -35, 0, 39, 78, 112, 137, 149, 144, 123, 86, 35, -24, -87, -146, -195, -226, -234, -217, -173, -106, -19, 79, 178, 268,
338, 376, 376, 333, 247, 122, -32, -204, -377, -530, -645, -704, -691, -593, -407, -133, 221, 642, 1108, 1594, 2071, 2512, 2888, 3176, 3356, 3418, 3356, 3176,
2888, 2512, 2071, 1594, 1108, 642, 221, -133, -407, -593, -691, -704, -645, -530, -377, -204, -32, 122, 247, 333, 376, 376, 338, 268, 178, 79, -19, -106, -173, -217, -234, -226, -195, -146, -87, -24, 35, 86, 123, 144, 149, 137, 112, 78, 39, 0, -35, -64, -84, -93, -91, -80, -62, -39, -14, 9, 29, 44, 53, 56, 52, 43, 31, 17, 2, -10, -20, -28, -31, -31, -27, -21, -14, -6, 1, 8, 13, 16, 16, 16, 13, 10, 5, 1, -2, -5, -8, -9, -9, -9, -7, -5, -2};
    float BANDPASS[] = {0, -5, -1, 9, 18, 16, 5, -2, 0, 8, 10, -1, -20, -28, -18, -2, 0, -14, -27, -18, 12, 39, 38, 14, 0, 16, 49, 57, 20, -34, -58, -34, 0, -8, -63, -110, -89, -8, 60, 55, 0, -20, 47, 151, 186, 104, -19, -64, 0, 70, 23, -139, -275, -247, -84, 40, 0, -135, -162, 24, 293, 401, 256, 35, 0, 191, 361, 237, -158, -494, -474, -180, 0, -200, -589, -683, -244, 410, 698, 414, 0, 98, 797, 1420, 1187, 111, -876, -853, 0, 361, -934, -3439, -5022, -3565, 958, 5999, 8191, 5999, 958, -3565, -5022, -3439, -934, 361, 0, -853, -876, 111, 1187, 1420, 797, 98, 0, 414, 698, 410, -244, -683, -589, -200, 0, -180, -474, -494, -158, 237, 361, 191, 0, 35, 256,
401, 293, 24, -162, -135, 0, 40, -84, -247, -275, -139, 23, 70, 0, -64, -19, 104, 186, 151, 47, -20, 0, 55, 60, -8, -89, -110, -63, -8, 0, -34, -58, -34, 20, 57, 49, 16, 0, 14, 38, 39, 12, -18, -27, -14, 0, -2, -18, -28, -20, -1, 10, 8, 0, -2, 5, 16, 18, 9, -1, -5};
    float HIGHPASS[] = {0, 7, 7, -1, -9, -6, 3, 10, 5, -6, -12, -4, 10, 14, 2, -14, -15, 1, 19, 16, -6, -25, -16, 12, 31, 14, -21, -36, -10, 31, 41, 3, -43, -44, 7, 56, 44, -21, -69, -41, 39, 82, 33, -60, -93, -19, 84, 100, 0, -110, -102, 26, 137, 98, -59, -163, -85, 100, 187, 63, -146, -206, -29, 198, 217, -17, -255, -218, 79, 315, 206, -157, -376, -175, 255, 436, 122, -377, -494, -37, 529, 546, -92, -728, -593, 295, 1009, 631, -641, -1469, -659, 1367, 2509, 677, -4135, -9356, 21157, -9356, -4135, 677, 2509, 1367, -659, -1469, -641, 631, 1009, 295, -593, -728, -92, 546, 529, -37, -494, -377, 122, 436, 255, -175, -376, -157, 206, 315, 79, -218, -255,
-17, 217, 198, -29, -206, -146, 63, 187, 100, -85, -163, -59, 98, 137, 26, -102, -110, 0, 100, 84, -19, -93, -60, 33, 82, 39, -41, -69, -21, 44, 56, 7, -44, -43, 3, 41, 31, -10, -36, -21, 14, 31, 12, -16, -25, -6, 16, 19, 1, -15, -14, 2, 14, 10, -4, -12, -6, 5, 10, 3, -6, -9, -1, 7, 7};

    short sample[Num_Amostras];

    for(i = 0; i < Num_Amostras; i++)
    {
        sample[i] = 0;
    }

    short n;
    short n_amost;
    short y, x, z;
    short entrada, saida;

    short Gb = 0, Gm = 9830, Ga = 19660;

    do
    {

        y=0;
        z = 0;
        x = 0;

        n_amost = fread(&entrada, sizeof(short), 1, Data_in);
        sample[0] = entrada;

        for(n=0; n<Num_Amostras; n++){

            x += HIGHPASS[n]*sample[n];
            y += LOWPASS[n]*sample[n];
            z += BANDPASS[n]*sample[n];
        }

        for (n = Num_Amostras-1; n>0; n--)
        {
            sample[n]=sample[n-1];
        }

        saida =  (y * Gb) + (x * Ga) + (z * Gm);

        fwrite(&saida, sizeof(short), 1, Data_out);

    }
    while (n_amost);

    fclose(Data_in);
    fclose(Data_out);

    return 0;
}
