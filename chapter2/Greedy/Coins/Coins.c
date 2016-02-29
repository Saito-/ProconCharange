#include <stdio.h>
#include <stdlib.h>

int names[6] = { 1, 5, 10, 50, 100, 500 };
int coins[6];
int ans[6];
int A;

int min2(int a, int b)
{
	return (a < b) ? a : b;
}

void init(char* fname)
{
	FILE* fp = fopen(fname, "r");
	fscanf(fp, "%d %d %d %d %d %d %d ", 
		coins, coins+1, coins+2, coins+3, coins+4, coins+5, &A);
	fclose(fp);
}

void solve()
{
	int i;
	for (i = 5; i >= 0; i--) {
		int tmp = min2(A / names[i], coins[i]);
		A -= tmp * names[i];
		ans[i] += tmp;
	}
}

void print()
{
	int i, num = 0;
	for (i = 0; i < 6; i++) {
		if (ans[i] != 0) {
			num += ans[i];
			printf("%d Yen, %d mai\n", names[i], ans[i]);
		}
	}
	printf("Total: %d mai\n", num);
}

int main(int argc, char* argv[])
{
	init(argv[1]);
	solve();
	print();

	return 0;
}
