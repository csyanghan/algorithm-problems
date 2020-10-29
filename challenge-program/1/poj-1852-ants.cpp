#include<iostream>
#include<algorithm>

using namespace std;

int main() {
  int times;
  cin >> times;
  while (times--) {
    int L, n;
    cin >> L >> n;
    int* x = new int[n];
    for (int i=0; i< n; i++) cin >> x[i];
    int minT = 0;
    for (int i=0; i<n; i++) {
      minT = max(minT, min(x[i], L-x[i]));
    }
    int maxT = 0;
    for (int i=0; i<n; i++) {
      maxT = max(maxT, max(x[i], L-x[i]));
    }
    cout << minT << " " << maxT << endl;
  }
  return 0;
}
