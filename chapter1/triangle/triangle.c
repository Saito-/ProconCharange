#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n;
int* a;

int max2(int a, int b)
{
	if (a > b) return a;
	else return b;
}

int max3(int a, int b, int c)
{
	if (a > b) 
		return max2(a, c);
	else 
		return max2(b, c);
}

int main(int argc, char* argv[])
{
	FILE* fp;
	char line[1024];
	char* ch = line+5;
	int i, j, k, ans=0;
	int edges[3] = { 0 };
	fp = fopen(argv[1], "r");
	fscanf(fp, "n = %d ", &n);
	a = (int*)malloc(sizeof(int)*n);
	fgets(line, 1024, fp);
	fclose(fp);
	for (i = 0; i < n; i++) {
		a[i] = atoi(ch);
		if (!(ch = strchr(ch, ','))) break;
		ch++;
	}

	for (i = 0; i < n; i++) {
		int edge1 = a[i];
		for (j = 0; j < n; j++) {
			if (i == j) continue;
			int edge2 = a[j];
			for (k = 0; k < n; k++) {
				if ((i == k) || (j == k)) continue;
				int edge3 = a[k];
				int perim = edge1 + edge2 + edge3;
				int max = max3(edge1, edge2, edge3);
				int rest = perim - max;
				if (max < rest && perim > ans) {
					ans = perim;
					edges[0] = edge1;
					edges[1] = edge2;
					edges[2] = edge3;
				}
			}
		}
	}
	

	if (ans == 0) {
		printf("0 (You cannot make triangle)\n");
	} else {
		printf("%d (%d, %d, %d)\n", ans, edges[0], edges[1], edges[2]);
	}
	free(a);
	return 0;
}
