#include <stdio.h>

int N = 3;
int L[3] = { 8, 5, 8 };

void swap(int* a, int* b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void solve()
{
	long long ans = 0;

	while (N > 1) {
		int mil1 = 0, mil2 = 1;
		if (L[mil1] > L[mil2]) swap(&mil1, &mil2);
		
		int i;
		for (i = 2; i < N; i++) {
			if (L[i] < L[mil1]) {
				mil2 = mil1;
				mil1 = i;
			}
			else if (L[i] < L[mil2]) {
				mil2 = i;
			}
		}

		int t = L[mil1] + L[mil2];
		ans += t;

		if (mil1 == N - 1) swap(&mil1, &mil2);
		L[mil1] = t;
		L[mil2] = L[N-1];
		N--;
	}
	printf("%lld\n", ans);
}

int main()
{
	solve(); return 0;
}
