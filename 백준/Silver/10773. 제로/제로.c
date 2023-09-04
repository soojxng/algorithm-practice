#include <stdio.h>

int s[100001];
int top = -1;
int sum = 0;

void push(int x) {
	s[++top] = x;
	sum += x;
	return;
}

void pop() {
	sum -= s[top--];
	return;
}

int main(void) {
	int k = 0;
	scanf("%d", &k);
	for (int i = 0; i < k; i++) {
		int n = 0;
		scanf("%d", &n);
		if (n == 0) {
			pop();
		}
		else {
			push(n);
		}
	}
	printf("%d\n", sum);
}