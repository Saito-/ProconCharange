#include <stdio.h>
#include <string.h>
#include <limits.h>

#define INF 1000000

int n = 4, W = 5;
int w[4] = { 2, 1, 3, 2 };
int v[4] = { 3, 2, 4, 2 };

int dp[4 + 1][4 * 5 + 1];

void init()
{
	int j;
	for (j = 1; j <= n * W; j++) 
		dp[0][j] = INF;
}

int min(int a, int b)
{
	return (a < b) ? a : b;
}

void solve() 
{
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j <= n * W; j++) {
			if (j < v[i]) 
				dp[i+1][j] = dp[i][j];
			else
				dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i]);
		}
	}
	int ans = 0;
	for (i = 0; i <= n * W; i++)
		if (dp[n][i] <= W) 
			ans = i;
	printf("%d\n", ans);
}

void print_dp()
{
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j <= n * W; j++) {
			if (dp[i][j] == INF)
				printf("INF ");
			else
				printf("%d ", dp[i][j]);
		}
		putchar('\n');
	}
}

int main() 
{
	init(); solve(); print_dp(); return 0;
}
