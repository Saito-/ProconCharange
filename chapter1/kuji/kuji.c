#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n, m;
int* k;
int* kk;

void swap(int* a, int* b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int binary_search(int key)
{
	int l = 0, r = (n*(n+1))/2;
	while (r - l >= 1) {
		int i = (l + r)/2;
		if (kk[i] == key) return 0;
		else if (kk[i] < key) l = i + 1;
		else r = i;
	}
	return 1;
}

void quick_sort(int left, int right)
{
	int i, j, pivot;
	i = left;
	j = right;
	pivot = kk[(left+right)/2];
	
	while (1) {
		while (kk[i] < pivot) i++;
		while (kk[j] > pivot) j--;
		if (i >= j) break;

		swap(kk+i, kk+j);
		i++;
		j--;
	}
	if (i - left >= 2) quick_sort(left, i-1);
	if (right - j >= 2) quick_sort(j+1, right);
}

int main(int argc, char* argv[])
{
	FILE* fp;
	char line[1024];
	char* ch = line+5;
	int i, j;
	
	fp = fopen(argv[1], "r");
	fscanf(fp, "n = %d ", &n);
	fscanf(fp, "m = %d ", &m);
	k = (int*)malloc(sizeof(int)*n);
	kk = (int*)malloc(sizeof(int)*((n*(n+1))/2));
	fgets(line, 1024, fp);
	fclose(fp);

	for (i = 0; i < n; i++) {
		k[i] = atoi(ch);
		if (!(ch = strchr(ch, ','))) break;
		ch++;
	}

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			kk[i * n + j] = k[i] + k[j];
		}
	}

	quick_sort(0, (n*(n+1))/2);

	int f = 1;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			f = binary_search(m - k[i] - k[j]);
			if (f == 0) break;
		}
	}

	if (f == 0) 
		printf("Yes\n");
	else
		printf("No\n");
	free(k); free(kk);
	return 0;
}
