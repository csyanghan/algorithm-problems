#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

// #define 关键字在C/C++中用作宏处理,基本作用如下, 宏定义不要以分号结尾
#define MAX_MN 1000

int n=3, m=9, k[MAX_MN]={1,3,5};

string solve() {
  int kk[MAX_MN * MAX_MN];
  string ans = "false";
  for (int c=0; c<n ; c++) {
    for (int d=0; d<n; d++) {
      kk[c*n+d] = k[c] + k[d];
    }
  }
  sort(kk, kk + n*n);
  for (int a=0; a<n;a++) {
    for (int b=0; b<n; b++) {
      if (binary_search(kk, kk+n*n, m-k[a]-k[b])) {
        ans = "true";
        break;
      }
    }
  }
  return ans;
}

int main() {
  cout << solve() << endl;
  return 0;
}