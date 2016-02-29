#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;
char *S, *T;
int head, tail;

void init(char* fname)
{
	int i;
	FILE* fp = fopen(fname, "r");
	char str[2000];
	
	fscanf(fp, "%d ", &N);

	S = (char*)malloc((N+1)*sizeof(char));
	T = (char*)malloc((N+1)*sizeof(char));
	S[N] = '\0'; T[N] = '\0';
	tail = N-1;
	fgets(str, 2000, fp);
	memcpy(S, str, N);

	fclose(fp);
}

void end()
{
	free(S); free(T);
}

void solve()
{
	int i;
	for (i = 0; i < N; i++) {
		char s = S[head];
		char e = S[tail];
		if (s < e) {
			T[i] = s;
			head++;
		} else {
			T[i] = e;
			tail--;
		}
	}
}

int main(int argc, char* argv[])
{
	init(argv[1]);
	solve();
	printf("T: %s\n", T);
	end();
	return 0;
}
