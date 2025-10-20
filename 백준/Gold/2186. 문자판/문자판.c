#include <stdio.h>
#include <string.h>

int n, m, k;
int L;
char board[101][101];
char word[81];
int dp[101][101][81];
int d[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int dfs(int x, int y, int wi){
    if(wi == L){
        return 1;
    }
    if(dp[x][y][wi] != -1){
        return dp[x][y][wi];
    }
    
    dp[x][y][wi] = 0;
    for(int di = 0; di < 4; di++){
        int nx = x;
        int ny = y;
        for(int w = 1; w < k+1; w++){
            nx += d[di][0];
            ny += d[di][1];
            if(0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] == word[wi]){
                dp[x][y][wi] += dfs(nx, ny, wi+1);
            }
        }
    }

    return dp[x][y][wi];
}

int main(){
    int cnt = 0;
    memset(dp, -1, sizeof(dp));

    scanf("%d %d %d", &n, &m, &k);
    for(int i = 0; i < n; i++){
        scanf("%s", board[i]);
    }
    scanf("%s", word);
    L = strlen(word);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(board[i][j] == word[0]){
                cnt += dfs(i, j, 1);
            }
        }
    }

    printf("%d", cnt);
}