#include <stdio.h>

int main()
{
	int n, cnt = 0;

	scanf("%d", &n);

	do
	{
		if (n % 5 == 0)
		{
			cnt = cnt + n / 5;
			n = 0;
		}
			
		else
		{
			n -= 3;
			cnt++;
		}
	} while (n > 0);

	if (n < 0)
		cnt = -1;
	
	printf("%d\n", cnt);

	return 0;
}