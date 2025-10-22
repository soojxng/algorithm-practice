#include <stdio.h>

typedef long long ll;
ll x[4], y[4];

int ccw(int i, int j, int k) {
    ll tmp = (x[j]-x[i])*(y[k]-y[i])-(x[k]-x[i])*(y[j]-y[i]);
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
        scanf("%lld %lld", &x[i], &y[i]);
    }
    int a = ccw(0, 1, 2) * ccw(0, 1, 3);
    int b = ccw(2, 3, 0) * ccw(2, 3, 1);

    printf("%d", (a <= 0 && b <= 0) ? 1 : 0);
}