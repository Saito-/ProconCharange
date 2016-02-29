#include <stdio.h>
#include <stdlib.h>

int n = 3, m = 3, M = 10000;
int a[3] = { 1, 2, 3 };

int dp[3 + 1][3 + 1];

void solve()
{
	int i, j;
	for (i = 0; i <= n; i++)
		dp[i][0] = 1;
	for (i = 0; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			if (j - a[i] - 1 >= 0)
				dp[i+1][j] = (dp[i+1][j-1]+dp[i][j]-dp[i][j-1-a[i]]+M) % M;
			else
				dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M;
		}
	}
	printf("%d\n", dp[n][m]);
}

void print()
{
	int i, j;
	for (i = 0; i <= n; i++) {
		for (j = 0; j <= m; j++) {
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
