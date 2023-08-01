#include <stdio.h>
#include <math.h>

int main()
{
	int m, n, cnt = 0, num;

	scanf("%d %d", &m, &n);

	for (int i = m; i <= n; i++)
	{
		num = sqrt((double)i);

		for (int j = 2; j <= num ; j++)
		{
			if (i % j == 0)
				cnt = 1;
		}

		if (cnt == 0 && i != 1)
			printf("%d\n", i);

		cnt = 0;
	}

	return 0;
}