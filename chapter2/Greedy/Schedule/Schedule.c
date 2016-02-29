#include <stdio.h>
#include <stdlib.h>

int N;
int *s, *f;
int *chk;

void init(char* fname)
{
	int i;
	FILE* fp = fopen(fname, "r");
	fscanf(fp, "%d ", &N);
	
	s = (int*)malloc(sizeof(int)*N);
	f = (int*)malloc(sizeof(int)*N);
	chk = (int*)calloc(N, sizeof(int));

	for (i = 0; i < N; i++) {
		fscanf(fp, "%d %d ", s+i, f+i);
	}
	fclose(fp);
}

void end()
{
	free(s); free(f); free(chk);
}

void solve()
{
	int i, tmp = f[0];
	chk[0] = 1;
	for (i = 1; i < N; i++) {
		if (s[i] > tmp) {
			chk[i] = 1;
			tmp = f[i];
		}
	}
}

void print()
{
	int i, num = 0;
	for (i = 0; i < N; i++) {
		if (chk[i] == 1) {
			printf("Work %d\n", i+1);
			num++;
		}
	}
	printf("Total: %d\n", num);
}

int main(int argc, char* argv[])
{
	init(argv[1]);
	solve();
	print();
	end();

	return 0;
}
