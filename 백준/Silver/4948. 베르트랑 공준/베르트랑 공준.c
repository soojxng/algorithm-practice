#include <stdio.h>
int main(void) {
	int n, a[260001] = { 0, }, cnt = 0;
	a[1] = 1;

	for (int i = 2; i <= 260000; i++) {
		for (int j = 2; i * j <= 260000; j++) {
			a[i * j] = 1;
		}
	}

	
	while (1) {
		scanf("%d", &n);

		if (n == 0)
            break;

		for (int i = n + 1; i <= 2 * n; i++) {
			if (a[i] == 0) {
				cnt++;
			}

		}

		printf("%d\n", cnt);
		cnt = 0;
		n = 0;
	}

	return 0;
}