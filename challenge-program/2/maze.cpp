#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

// @Author: Hanyang
// @Date: 2020-11-02

#define MAX_N 100
#define MAX_M 100

const int INF = 1e8;

typedef pair<int, int> P;  // 用来表示状态
char maze[MAX_N][MAX_M+1]; // 表示迷宫的字符串的数组
int N, M;
int sx, sy;  // start coordinate
int gx, gy;  // goal coordinate

int d[MAX_N][MAX_M];  // 到各个位置的最短距离的数组
int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1}; // 方向

int bfs() {
  queue<P> que;

  // 把所有的位置都初始化为INF
  for(int i=0; i<N; i++) {
    for(int j=0; j<M; j++) d[i][j] = INF;
  }

  // 将起点加入队列，并把这一地点的距离设置为0
  que.push(P(sx, sy));
  d[sx][sy] = 0;
  
  // 不断循环直到队列的长度为0
  while (que.size())
  {
    // 从队列的最前端取出元素
    P p = que.front();
    que.pop();

    // 如果取出的状态已经是终点，则结束搜索
    if (p.first == gx && p.second == gy) break;
    // 四个方向的循环
    for (int i = 0; i < 4; i++) {
      // 移动之后的位置记为(nx, ny)
      int nx = p.first + dx[i], ny = p.second + dy[i];
      // 判断是否可以移动以及是否已经访问过(d[nx][ny]!=INF即为已经访问过)
      if (0 <= nx && nx < N && 0 <= ny && ny < M && maze[nx][ny] != '#' && d[nx][ny] == INF) {
        // 可以移动的话，则加入到队列，并且到该位置的距离确定为到p的距离+1 que.push(P(nx, ny));
        d[nx][ny] = d[p.first][p.second] + 1;
      }
    }
  }
  return d[gx][gy];
}

int main() {
  int res = bfs();
  printf("%d\n", res);
}