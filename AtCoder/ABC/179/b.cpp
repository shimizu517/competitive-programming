#include <iostream>
#include <string>
#include <stdlib.h>
#include <stack>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>

static const int MAX = 100000;
static const int INFTY = (1 << 20);
using namespace std;

int main()
{
  int N;
  cin >> N;
  vector<vector<int>> d(N, vector<int>(2));
  for (int i = 0; i < N; i++)
  {
    cin >> d[i][0];
    cin >> d[i][1];
  }

  int count = 0;
  for (int i = 0; i < N; i++)
  {
    if (d[i][0] == d[i][1])
      count++;
    else
      count = 0;
    if (count >= 3)
    {
      printf("Yes");
      return 0;
    }
  }
  printf("No");
  return 0;
}