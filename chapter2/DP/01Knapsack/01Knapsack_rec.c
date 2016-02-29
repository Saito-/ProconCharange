#include <stdio.h>
#include <string.h>

int n = 4, W = 5;
int w[4] = { 2, 1, 3, 2 };
int v[4] = { 3, 2, 4, 2 };

int dp[4 + 1][5 + 1];

int max(int a, int b)
{
	return (a > b) ? a : b;
}

int m(int i, int j)
{
	if (dp[i][j] >= 0) return dp[i][j];

	int res;
	if (i == n) {
		res = 0;
	} else if (j < w[i]) {
		res = m(i+1, j);
	} else {
		res = max(m(i+1, j), m(i+1, j - w[i]) + v[i]);
	}
	return dp[i][j] = res;
}

void solve() 
{
	memset(dp, -1, sizeof(dp));
	printf("%d\n", m(0, W));
}

int main() 
{
	solve(); return 0;
}
