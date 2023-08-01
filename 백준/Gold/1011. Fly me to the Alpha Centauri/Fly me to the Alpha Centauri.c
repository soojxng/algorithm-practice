#include <stdio.h>

void count(int* pn, int* pcnt, int* pk)
{
	while (*pn > *pk)
	{
		*pn = *pn - *pk;
		(*pcnt)++;

		if (*pn <= *pk)
		{
			(*pk)++;
			break;
		}
			
		*pn = *pn - *pk;
		(*pcnt)++;
		(*pk)++;
	}

	return;
}

void count2(int* pn, int* pcnt, int* pk)
{
	for (*pk = *pk; *pk > 0; (*pk)--)
	{
		while (*pn >= *pk)
		{
			*pn = *pn - *pk;
			(*pcnt)++;
		}
	}

	return;
}

int main()
{
	int t, x, y, cnt = 0, k = 1, n;

	int* pn, * pcnt, * pk;

	pn = &n;
	pcnt = &cnt;
	pk = &k;

	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		scanf("%d %d", &x, &y);

		n = y - x;

		count(pn, pcnt, pk);
		count2(pn, pcnt, pk);

		printf("%d\n", cnt);

		cnt = 0;
		k = 1;
	}

	return 0;
}