#include <stdio.h>

int x[4], y[4];

int ccw(int i, int j, int k) {
    int tmp = (x[j]-x[i])*(y[k]-y[i])-(x[k]-x[i])*(y[j]-y[i]);
    if (tmp < 0) {
        return -1;
    } else if (tmp == 0) {
        return 0;
    } else {
        return 1;
    }
}

int main(void) {
    for (int i = 0; i < 4; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }
    int a = ccw(0, 1, 2) * ccw(0, 1, 3);

    printf("%d", a == -1 ? 1 : 0);
}