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

void solve() 
{
	int i, j;
	for (i = 1; i <= n; i++) {
		for (j = 0; j <= W; j++) {
			if (j < w[i-1]) 
				dp[i][j] = dp[i-1][j];
			else
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1]);
		}
	}
	printf("%d\n", dp[4][5]);
}

void print_dp()
{
	int i, j;
	for (i = 0; i <= n; i++) {
		for (j = 0; j <= W; j++) {
			printf("%d ", dp[i][j]);
		}
		putchar('\n');
	}
}

int main() 
{
	solve(); print_dp(); return 0;
}
