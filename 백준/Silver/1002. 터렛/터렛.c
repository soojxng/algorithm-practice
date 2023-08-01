#include <stdio.h>
#include <math.h>

int main(void)
{
	int n;
	double x1, y1, x2, y2, r1, r2, d, r;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);

		d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));

		if (r1 - r2 > 0)
			r = r1 - r2;
		else
			r = r2 - r1;

		if (d == 0 && r1 == r2)
			printf("-1\n");
		else if (r < d && d < r1 + r2)
			printf("2\n");
		else if (r1 + r2 == d || r == d)
			printf("1\n");
		else
			printf("0\n");
	}

	return 0;
}