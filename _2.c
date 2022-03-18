#include <stdio.h>

int main() {
    char pokemon[50];
    printf("Which starter pokemon do you want as your partner?\n");
    scanf("%s", &pokemon);
    printf("%s", pokemon);
    int x = pokemon == "aaa";
    printf("%d", x);
    if(pokemon == "aaa") {
        printf("Congratulations,you have chosen the Fire type pokemon!\n");
    }
    else if(pokemon == "bbb") {
        printf("Congratulations,you have chosen the Water type pokemon!\n");
    }
    else if(pokemon == "ccc") {
        printf("Congratulations,you have chosen the Grass type pokemon\n");
    }
    else {
        printf("This pokemon does not exist!\n");
    }
    return  0;
}