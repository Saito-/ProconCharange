#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int N, M;
char** map;

void init(char* fname)
{
	int i, j;
	char line[128];
	FILE* fp = fopen(fname, "r");
	fscanf(fp, "N=%d, M=%d ", &N, &M);
	map = (char**)malloc(sizeof(char*)*N);
	for (i = 0; i < N; i++) {
		map[i] = (char*)malloc(sizeof(char)*(M+1));
		map[i][M] = '\0';
	}
	for (i = 0; i < N; i++) {
		fgets(line, 128, fp);
		for (j = 0; j < M; j++) {
			map[i][j] = line[j];
		}
	}
	fclose(fp);
}

void end()
{
	int i;
	for (i = 0; i < N; i++) 
		free(map[i]);
	free(map);
}

void print_map()
{
	int i, j;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) 
			putchar(map[i][j]);
		putchar('\n');
	}
}

void DFS(int x, int y)
{
	int dx, dy;
	map[x][y] = '.';

	for (dx = -1; dx <= 1; dx++) {
		for (dy = -1; dy <= 1; dy++) {
			int nx = x + dx;
			int ny = y + dy;
			bool in_map_x = nx >= 0 && nx < N;
			bool in_map_y = ny >= 0 && ny < M;
			if (in_map_x && in_map_y && map[nx][ny] == 'W') 
				DFS(nx, ny);
		}
	}
}

int search()
{
	int i, j, count=0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			if (map[i][j] == 'W') {
				DFS(i, j);
				count++;
			}
		}
	}
	return count;
}

int main(int argc, char* argv[])
{
	init(argv[1]);

	print_map();
	printf("Number of Lake: %d\n", search());

	end();
	return 0;
}
