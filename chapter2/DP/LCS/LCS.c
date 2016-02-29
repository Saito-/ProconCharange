#include <stdio.h>

int n = 4, m = 4;
char s[5] = " abcd", t[5] = " becd";
int dp[4+1][4+1];

int max(int a, int b)
{
	return (a > b) ? a : b;
}

void solve()
{
	int i, j;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= m; j++) {
			if (s[i] == t[j]) 
				dp[i][j] = dp[i-1][j-1] + 1;
			else
				dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
		}
	}
	printf("%d\n", dp[n][m]);
}

int main()
{
	solve(); return 0;
}
