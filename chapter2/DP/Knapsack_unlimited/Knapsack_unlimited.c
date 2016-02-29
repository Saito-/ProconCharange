#include <stdio.h>
#include <stdlib.h>

int n = 3, W = 7;
int w[3] = { 3, 4, 2 };
int v[3] = { 4, 5, 3 };

int DP[4][8];

int max(int a, int b)
{
	return (a > b) ? a : b;
}

void solve()
{
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j <= W; j++) {
			if (j < w[i])
				DP[i+1][j] = DP[i][j];
			else
				DP[i+1][j] = max(DP[i][j], DP[i+1][j-w[i]] + v[i]);
		}
	}
	printf("%d\n", DP[n][W]);
}

int main(int argc, char* argv[])
{
	solve();
	return 0;
}
