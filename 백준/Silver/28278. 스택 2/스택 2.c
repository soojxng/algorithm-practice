#include <stdio.h>

int s[1000001];
int top = -1;

void command1() {
	int x = 0;
	scanf("%d", &x);
	s[++top] = x;
	return;
}

void command2() {
	if (top != -1) {
		printf("%d\n", s[top--]);
	}
	else {
		printf("-1\n");
	}
	return;
}

void command3() {
	printf("%d\n", top + 1);
	return;
}

void command4() {
	if (top == -1)
		printf("1\n");
	else
		printf("0\n");
	return;
}

void command5() {
	if (top != -1) {
		printf("%d\n", s[top]);
	}
	else {
		printf("-1\n");
	}
	return;
}

void select() {
	int m = 0;
	scanf("%d", &m);
	switch (m) {
	case 1:
		command1();
		break;
	case 2:
		command2();
		break;
	case 3:
		command3();
		break;
	case 4:
		command4();
		break;
	case 5:
		command5();
		break;
	}
	return;
}

int main(void) {
	int n = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		select();
	}
	return 0;
}