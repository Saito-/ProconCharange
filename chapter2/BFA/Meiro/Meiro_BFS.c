#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <limits.h>

typedef struct {
	int x;
	int y;
} Point2D;

typedef struct queue {
	Point2D* que;
	int size;
	int mem_size;
	int front;
	bool (*enqueue)(struct queue* self, Point2D p);
	Point2D (*dequeue)(struct queue* self);
	void (*print)(struct queue* self);
} queue_t;

int N, M;
char** map;
int** dist;
Point2D start, goal;
queue_t* q;
int dx[4] = { 1, 0,-1, 0 };
int dy[4] = { 0, 1, 0,-1 };

bool que_enqueue(queue_t* self, Point2D p)
{
	if (self->size == self->mem_size) return false;
	
	self->que[(self->size+self->front)%self->mem_size] = p;
	self->size++;
	return true;
}

Point2D que_dequeue(queue_t* self)
{
	Point2D p = self->que[self->front];
	self->size--;
	self->front = (self->front + 1) % self->mem_size;
	return p;
}

void p2d_print(Point2D p)
{
	printf("(%d, %d) ", p.x, p.y);
}

void que_print(queue_t* self)
{
	int i;
	for (i = 0; i < self->size; i++) {
		p2d_print(self->que[(i + self->front) % self->mem_size]);
	}
	putchar('\n');
}

queue_t* new_queue(int mem_size)
{
	queue_t* q = (queue_t*)malloc(sizeof(queue_t));
	
	q->que = (Point2D*)malloc(sizeof(Point2D)*mem_size);
	q->size = 0;
	q->mem_size = mem_size;
	q->enqueue = que_enqueue;
	q->dequeue = que_dequeue;
	q->print = que_print;

	return q;
}

void destroy_queue(queue_t* q)
{
	free(q->que);
	free(q);
}

void init(char* fname)
{
	FILE* fp = fopen(fname, "r");
	char line[128];
	int i, j;
	fscanf(fp, "N=%d,M=%d\n", &N, &M);
	
	q = new_queue(N*M);
	map = (char**)malloc(sizeof(char*)*N);
	dist = (int**)malloc(sizeof(int*)*N);
	
	for (i = 0; i < N; i++) {
		map[i] = (char*)malloc(sizeof(char)*(M+1));
		dist[i] = (int*)malloc(sizeof(int)*M);
		map[i][M] = '\0';
		for (j = 0; j < M; j++) {
			dist[i][j] = INT_MAX;
		}
	}

	for (i = 0; i < N; i++) {
		fgets(line, 128, fp);
		for (j = 0; j < M; j++) {
			map[i][j] = line[j];
			if (line[j] == 'S') {
				start.x = i;
				start.y = j;
				q->enqueue(q, start);
				dist[i][j] = 0;
			}
			if (line[j] == 'G') {
				goal.x = i;
				goal.y = j;
			}
		}
	}

	fclose(fp);
}

void end()
{
	int i;
	for (i = 0; i < N; i++) {
		free(map[i]);
		free(dist[i]);
	}
	free(map); free(dist);
	destroy_queue(q);
}

int BFS()
{
	int i, j;
	while (q->size >= 0) {
		Point2D cur = q->dequeue(q);
		if (cur.x == goal.x && cur.y == goal.y) break;
		for (i = 0; i < 4; i++) {
			int nx = cur.x + dx[i];
			int ny = cur.y + dy[i];
			bool in_mapx = nx >= 0 && nx < N;
			bool in_mapy = ny >= 0 && ny < M;
			if (in_mapx && in_mapy && map[nx][ny] != '#' && dist[nx][ny] == INT_MAX) {
				Point2D p2;
				p2.x = nx;
				p2.y = ny;
				q->enqueue(q, p2);
				dist[nx][ny] = dist[cur.x][cur.y] + 1;
			}
		}
	}
	return dist[goal.x][goal.y];
}

void print_map()
{
	int i, j;
	for (i = 0; i < N; i++) {
		for (j = 0; j < M; j++) {
			putchar(map[i][j]);
		}
		putchar('\n');
	}
	putchar('\n');
}

int main(int argc, char* argv[])
{
	init(argv[1]);

	print_map();

	printf("Distance from start to goal: %d\n", BFS());

	end();
	return 0;
}
