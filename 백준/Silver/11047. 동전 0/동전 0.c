#include <stdio.h>

int main(void) {
	int n, k, x = 0;
	scanf("%d %d", &n, &k);

	int arr[15];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	int cnt = 0;
	while (k != 0) {
		n--;
		cnt = cnt + (k / arr[n]);
		k = k % arr[n];
	}
	printf("%d\n", cnt);
	return 0;
}