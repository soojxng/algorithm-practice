#include <stdio.h>

int q[1000000] = { 0 };
int front = -1;
int rear = -1;

void enqueue(int x) {
	q[++rear] = x;
	return;
}

int dequeue() {
	return q[++front];
}

int main(void) {
	int n;
	int x;
	scanf("%d", &n);
	rear = n - 1;
	for (int i = 0; i < n; i++) {
		q[i] = i + 1;
	}
	while (rear - front != 1) {
		x = dequeue();
		x = dequeue();
		enqueue(x);
	}
	printf("%d\n", q[++front]);
	return 0;
}