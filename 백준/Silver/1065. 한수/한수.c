#include <stdio.h>

void check(int num)
{
	int a = 0, b = 0, result = 99;

	for (int i = 100; i <= num; i++)
	{
		a = ((i / 10) - (i / 100 * 10)) - (i / 100);
		b = i % 10 - ((i / 10) - (i / 100 * 10));
		if (a == b)
			result++;
	}

	printf("%d", result);

	return;
}

int main()
{
	int num;

	scanf("%d", &num);

	if (num < 100)
		printf("%d", num);
	else
		check(num);

	return 0;
}