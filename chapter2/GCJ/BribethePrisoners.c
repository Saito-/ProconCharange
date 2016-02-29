#include <stdio.h>
#include <limits.h>

int P = 20, Q = 3;
int A[3 + 2] = { 0, 3, 6, 14, 21 };

int dp[3+1][3+2];

int min(int a, int b)
{
	return (a < b) ? a : b;
}

void solve()
{
	int q, w, i, k;
	for (q = 0; q <= Q; q++) {
		dp[q][q+1] = 0;
	}

	for (w = 2; w <= Q + 1; w++) {
		for (i = 0; i + w <= Q + 1; i++) {
			int j = i + w, t = INT_MAX;

			for (k = i + 1; k < j; k++) 
				t = min(t, dp[i][k] + dp[k][j]);

			dp[i][j] = t + A[j] - A[i] - 2;
		}
	}
	printf("%d\n", dp[0][Q+1]);
}

int main()
{
	solve();
	return 0;
}
