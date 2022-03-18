#include<stdio.h>
#include<math.h>

double fact(int x) {
    if (x == 0) {
        return 1;
    }

    double f = x * fact(x-1);
    return f;
}

int main() {
    printf("%lf\n", fact(25));
    // printf("%lf\n", pow(2, 64));


    if (1) {
        printf('999');
    }
    else {
        if (0) {
            printf('000');
        }
    }
    else {
        printf('333')
    }
    

    return 0;
}