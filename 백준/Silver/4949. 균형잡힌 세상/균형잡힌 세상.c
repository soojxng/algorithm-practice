#include <stdio.h>

int s[102];
int top = -1;

void push(int x) {
	s[++top] = x;
	return;
}

int pop() {
	if (top == -1)
		return 0;
	return s[top--];
}

int main(void) {
	while (1) {
		char str[101];
		int i = 0;
		int x;
		int flag = 0;
		fgets(str, 102, stdin);
		if (str[0] == '.' && str[1] == '\n')
			break;
		while(str[i] != NULL) {
			switch (str[i]) {
			case '(':
				push(1);
				break;
			case '[':
				push(2);
				break;
			case ')':
				x = pop();
				if (x != 1)
					flag++;
				break;
			case ']':
				x = pop();
				if (x != 2)
					flag++;
				break;
			default:
				break;
			}
			if (flag > 0)
				break;
			i++;
		}
		if (top != -1)
			flag++;
		if (flag == 0)
			printf("yes\n");
		else
			printf("no\n");
		top = -1;
		flag = 0;
		i = 0;
	}
	return 0;
}