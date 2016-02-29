#include <stdio.h>
#include <stdlib.h>

int n = 5;
int a[5] = {4, 2, 3, 1, 5};

int dp[5 + 1]; 

int max(int a, int b)
{
	return (a > b) ? a : b;
}

void solve()
{
	int i, j;
	dp[0] = 0;
	for (i = 0; i < n; i++) {
		dp[i+1] = 1;
		for (j = 0; j < i; j++) 
			if (a[j] < a[i])
				dp[i+1] = max(dp[i+1], dp[j] + 1);
	}
	printf("%d\n", dp[n]);
}

int main(int argc, char* argv[])
{
	solve();
	return 0;
}
