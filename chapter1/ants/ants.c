#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int L, n;
int* x;

int max2(int a, int b)
{
	if (a > b) 
		return a;
	else
		return b;
}

int min2(int a, int b)
{
	if (a < b)
		return a;
	else
		return b;
}

int max_arr(int* a)
{
	int i;
	int max = a[0];
	for (i = 1; i < n; i++) {
		if (a[i] > max)
			max = a[i];
	}
	return max;
}

void calc_min()
{
	int i, ans;
	int* dists;
	dists = (int*)malloc(sizeof(int)*n);
	for (i = 0; i < n; i++) {
		int min = min2(x[i], L - x[i]);
		dists[i] = min;
	}
	ans = max_arr(dists);
	printf("min = %d\n", ans);
	free(dists);
}

void calc_max()
{
	int i, ans;
	int* dists;
	dists = (int*)malloc(sizeof(int)*n);
	for (i = 0; i < n; i++) {
		int max = max2(x[i], L - x[i]);
		dists[i] = max;
	}
	ans = max_arr(dists);
	printf("max = %d\n", ans);
	free(dists);
}

int main(int argc, char* argv[])
{
	FILE* fp;
	char line[1024];
	char* ch = line+5;
	int i;
	fp = fopen(argv[1], "r");
	fscanf(fp, "L = %d ", &L);
	fscanf(fp, "n = %d ", &n);
	x = (int*)malloc(sizeof(int)*n);
	fgets(line, 1024, fp);
	fclose(fp);
	for (i = 0; i < n; i++) {
		x[i] = atoi(ch);
		if (!(ch = strchr(ch, ','))) break;
		ch++;
	}
	
	calc_min();
	calc_max();
	free(x);
	return 0;
}
