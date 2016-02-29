#include <stdio.h>
#include <stdlib.h>

int n = 4, m = 3, M = 10000;

int dp[3 + 1][4 + 1];

void solve()
{
	int i, j;
	dp[0][0] = 1;
	for (i = 1; i <= m; i++) {
		for (j = 0; j <= n; j++) {
			if (j - i >= 0) 
				dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % M;
			else 
				dp[i][j] = dp[i-1][j];
		}
	}
	printf("%d\n", dp[m][n]);
}

void print()
{
	int i, j;
	for (i = 0; i <= m; i++) {
		for (j = 0; j <= n; j++) {
			printf("%d ", dp[i][j]);
		}
		putchar('\n');
	}
}

int main(int argc, char* argv[])
{
	solve();
	print();
	return 0;
}
