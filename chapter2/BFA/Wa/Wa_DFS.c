#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int n, k;
int* a;

void init(char* fname)
{
	FILE* fp = fopen(fname, "r");
	char line[1024];
	char* ch = line+3;
	int i;

	fscanf(fp, "n=%d ", &n);
	a = (int*)malloc(sizeof(int)*n);
	fgets(line, 1024, fp);
	for (i = 0; i < n; i++) {
		a[i] = atoi(ch);
		if (!(ch = strchr(ch, ','))) break;
		ch++;
	}

	fscanf(fp, "k=%d ", &k);

	fclose(fp);
}

void end()
{
	free(a);
}

bool DFS(int i, int sum)
{
	printf("i = %d, sum = %d\n", i, sum);
	if (i == n) return sum == k;
	
	if (DFS(i+1, sum)) return true;

	if (DFS(i+1, sum + a[i])) return true;

	return false;
}

int main(int argc, char* argv[])
{
	init(argv[1]);

	
	if (DFS(0, 0))
		printf("Yes\n");
	else
		printf("No\n");

	end();
	
	return 0;
}
