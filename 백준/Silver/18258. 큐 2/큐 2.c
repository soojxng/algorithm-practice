#include <stdio.h>
#include <string.h>

int q[2000001] = { 0 };
int f = -1;
int r = -1;

int empty() {
	return f == r;
}

void push(int x) {
	q[++r] = x;
	return;
}

int pop() {
	if (empty())
		return -1;
	else
		return q[++f];
}

int size() {
	return r - f;
}

int front() {
	if (empty())
		return -1;
	else
		return q[f + 1];
}

int back() {
	if (empty())
		return -1;
	else
		return q[r];
}

void menu() {
	char s[6];
	scanf("%s", &s);
	int x;
	if (!strcmp(s, "push")) {
		scanf("%d", &x);
		push(x);
	}
	else if (!strcmp(s, "pop")) {
		x = pop();
		printf("%d\n", x);
	}
	else if (!strcmp(s, "size")) {
		x =size();
		printf("%d\n", x);
	}
	else if (!strcmp(s, "empty")) {
		x = empty();
		printf("%d\n", x);
	}
	else if (!strcmp(s, "front")) {
		x = front();
		printf("%d\n", x);
	}
	else if (!strcmp(s, "back")) {
		x = back();
		printf("%d\n", x);
	}
	return;
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		menu();
	}
	return 0;
}