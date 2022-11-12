#include "main.h"
#include <stdio.h>

/**
 * main - Prints the number of args
 * @argc: argument count
 * @argv: argument vector
 *
 * Return: Always zero
 */
int main(int argc, char *argv[])
{
int i;

if (argc == 1)
printf("%d\n", argc - 1);
else
{
for (i = 0; *argv; i++, argv++)
;

printf("%d\n", i - 1);
}

return (0);
}
