#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    double float_increment = 0.0000000000019346;
    double start = 57.240000;
    double floating_point = start;
    long long i;
    long long operations = 1000000000;
    for (i = 0; i < operations; ++i) {
        floating_point += float_increment;
    }   
    printf("Salut, ca va bien\n");
    printf("%lf\n", floating_point);

    return EXIT_SUCCESS;
}
