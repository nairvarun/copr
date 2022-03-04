#include <stdio.h>
#include <stdlib.h>
#include <math.h>
// #include <pthreads.h>

#define UPPER_LIM 20000000
#define MIL 1000000

void writePrimes() {
    FILE *fptr_prime;

    static int num[UPPER_LIM] = {0};
    static int prime[MIL];
    int mrt = sqrt(UPPER_LIM);

    for (int i = 2; i <= mrt; ++i) {
        if (num[i] == 0) {
            for (int j = i*i; j < UPPER_LIM; j += i) {
                num[j] = 1;
            }
        }
    }

    fptr_prime = fopen("./prime.txt", "w");

    if(fptr_prime == NULL) {
        printf("Error!");
        exit(1);
    }

    for (int i = 2, j = 0; i < UPPER_LIM, j < MIL; ++i) {
        if (!num[i]) {
            if (j < MIL) {
                fprintf(fptr_prime, "%d\n", i);
                ++j;
            } else {
                break;
            }
        }
    }
    fclose(fptr_prime);
}

void writeOdds() {
    FILE *fptr_odd;

    fptr_odd = fopen("./odd.txt", "w");

    if (fptr_odd == NULL) {
        printf("Error!");
        exit(1);
    }

    for (int i = 1; i < 2000000; i += 2) {
        fprintf(fptr_odd, "%d\n", i);
    }

    fclose(fptr_odd);
}

int main()
{
    int num;
    writeOdds();
    writePrimes();
    return 0;
}
