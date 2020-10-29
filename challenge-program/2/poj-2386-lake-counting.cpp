#include<iostream>
#include<string>

using namespace std;

// 注意这个地方不要只设置成100,稍微设置的大一点
#define MAX_N 105
#define MAX_M 105

char fields[MAX_N][MAX_M];
int N,M;

int dfs(int x, int y) {
  fields[x][y] = '.';
  for(int dx=-1; dx<=1; dx++) {
    for (int dy=-1; dy<=1; dy++) {
      int nx = x+dx, ny = y+dy;
      if (nx >=0 && nx < N && ny >=0 && ny<M && fields[nx][ny] == 'W') dfs(nx, ny);
    }
  }
  return 0;
}

int main() {
  cin >> N >> M;
  for(int i=0;i<N;i++)
    scanf("%s",fields[i]);
  int ans = 0;
  for(int i=0; i<N; i++) {
    for(int j=0; j<M; j++) {
      if (fields[i][j] == 'W') {
        dfs(i,j);
        ans ++;
      }
    }
  }
  cout << ans << endl;
  return 0;
}
