#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int W = 10, H = 10, N = 5;
int X1[5] = { 1, 1, 4, 9, 10 };
int X2[5] = { 6, 10, 4, 9, 10 };

int compress(int* x1, int* x2, int w)
{
	vector<int> xs;
	for (int i = 0; i < N; i++) {
		for (int d = -1; d <= 1; ++d) {
			int tx1 = x1[i] + d;
			int tx2 = x2[i] + d;
			if (1 <= tx1 && tx1 <= w)
				xs.push_back(tx1);
			if (1 <= tx2 && tx2 <= w)
				xs.push_back(tx2);
		}
	}

	sort(xs.begin(), xs.end());
	xs.erase(unique(xs.begin(), xs.end()), xs.end());

	for (int i = 0; i < N; i++) {
		x1[i] = find(xs.begin(), xs.end(), x1[i]) - xs.begin();
		x2[i] = find(xs.begin(), xs.end(), x2[i]) - xs.begin();
	}
	return xs.size();
}

int main()
{
	W = compress(X1, X2, W);
	printf("%d\n", W);
	return 0;
}
