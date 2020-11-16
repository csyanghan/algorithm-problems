#include<iostream>
#define MAX_N 2000

using namespace std;


int N;
char s[MAX_N+1];

int main() {
  cin >> N;
  int i=0;
  while(i < N) {
    cin >> s[i];
    i++;
  }
  int a = 0, b=N-1;
  while (a <= b)
  {
    bool left = false;
    for (int i=0; a+i <=b; i++) {
      if (s[a+i] < s[b-i]) {
        left = true;
        break;
      } else if (s[a+i] > s[b-i]) {
        left = false;
        break;
      }
    }
    if(left) cout << s[a++];
    else cout << s[b--];
    if (N>80 && (a+N-b-1) % 80 == 0) cout << endl;
  }
  cout << endl;
  return 0;
}