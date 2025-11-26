#include <stdio.h>

typedef unsigned int ui;

#define LEN (33554432/32+1)

ui visited[LEN];

int main(void) {
    int x;
    while(scanf("%d", &x) == 1) {
        ui i = x / 32;
        ui j = x % 32;
        ui k = 1u << j;

        if(!(visited[i] & k)) {
            visited[i] |= k;
            printf("%d ", x);
        }
    }

    return 0;
}