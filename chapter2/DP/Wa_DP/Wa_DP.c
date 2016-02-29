#include <stdio.h>
#include <stdlib.h>

int n = 3, K = 17;
int a[3] = {3, 5, 8};
int m[3] = {3, 2, 2};

int dp[17+1];
void init()
{
	int i;
	dp[0] = 0;
	for (i = 1; i <= K; i++)
		dp[i] = -1;
}

void solve() {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j <= K; j++) {
			if (dp[j] >= 0) 
				dp[j] = m[i];
			else if (j < a[i] || dp[j - a[i]] <= 0)
				dp[j] = -1;
			else
				dp[j] = dp[j - a[i]] - 1;
		}
	}
	if (dp[K] >= 0)
		printf("yes\n");
	else
		printf("no\n");
}

int main(int argc, char* argv[])
{
	init();
	solve();
	return 0;
}
