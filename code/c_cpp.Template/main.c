#include <stdio.h>


int add(int a, int b)
{
    return a + b;
}

int main()
{
    int a = 10, b = 20;
    int c = add(a, b);
    printf("%d\n",c);

    return 0;
}