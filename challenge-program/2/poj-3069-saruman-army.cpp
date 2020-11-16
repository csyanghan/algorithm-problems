#include<iostream>
#include<algorithm>
#define MAX_N 1000
using namespace std;

int N, R;
int X[MAX_N+1];

void solve() {
  cin >> R >> N;
  while (N !=-1 && R !=-1) {
    for(int i=0; i<N; i++) cin >> X[i];
    sort(X, X+N);
    int i=0, res = 0;
    while (i<N) {
      //  s是没有覆盖的最左边的点
      int s = X[i++];
      while(i<N && X[i] <= s+R) i++;
      
      // p是新加上标记的点
      int p = X[i-1];
      while (i<N && X[i] <= p+R) i++;
      res++;
    }
    cout << res << endl;
    cin >> R >> N;
  }
}

int main() {
  solve();
  return 0;
}