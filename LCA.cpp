#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <vector>
#include <deque>

#include <cstring>
int N, M; // N: 노드개수, M: 질문의 개수
int a, b;

std::vector<int> AL[100001]; // 인접 리스트
int Depth[100001]; // 깊이 저장 -> dfs or bfs

int Parent[18][100001]; // 현재 정점에서 2의 K제곱번째 부모의 정점 번호 저장

int LCA(int, int);

int main() { // 여러 개의 테스트케이스를 돌릴 때는 초기화에 신경써야 한다.(전역변수)
	scanf("%d", &N);
	for (int i = 1;i < N;i++) {
		scanf("%d %d", &a, &b);
		AL[a].push_back(b);
		AL[b].push_back(a);
	}

	// 전역변수로 정의된 배열을 모두 0이나 -1로 초기화하는 방법
	memset(Parent, 0, sizeof(Parent));

	 // BFS 를 이용하여 Depth 구함. 탐색의 시작은 Root
	for (int i = 1;i <= N;i++) Depth[i] = -1;
	std::deque<int> Q; // deque 대신 queue를 써도 된다.
	Q.push_back(1);
	Depth[1] = 0;
	while(!Q.empty()) {
		int curr = Q.front();
		Q.pop_front();
		for (int next : AL[curr]) {
			if (Depth[next] == -1) { // 미방문시 탐색
				Q.push_back(next);
				Depth[next] = Depth[curr] + 1;
				Parent[0][next] = curr; // !!!!
			}
		}
	}

	// 점핑 테이블 (희소 테이블) 을 만들기
	for (int r = 1;r < 18;r++) {
		for (int i = 1;i <= N;i++) {
			Parent[r][i] = Parent[r - 1][Parent[r - 1][i]]; // Parent[r][i]는 Parent[r-1][i]의 2^(r-1) 번째 부모
		}
	}

	scanf("%d", &M);
	for (int i = 0;i < M;i++) {
		scanf("%d %d", &a, &b);
		// !!!a, b의 LCA 구하여 출력!!!
		printf("%d\n", LCA(a, b));
	}
	return 0;
}

int LCA(int a, int b) {
	// Step 1 : Depth 맞추기
	// 항상 a의 depth가 크도록 함.
	if (Depth[a] < Depth[b]) { // tmp를 써서 swap 하는 것을 적극적으로 권장
		// 다른 것은 퍼포먼스가 좋지 않기 때문이다. 즉 연산이 나쁘다.
		int tmp=a; // tmp를 써서 하는 것이 매우 빠르다.
		a = b;
		b = tmp;
	}
	int diff = Depth[a] - Depth[b];
	// diff를 줄여서 0으로 만들면 a가 b가 있는 곳으로 올라간다.
	// diff 가 10이면 10=2^3+2^1. 그런데 10을 2진수로 표현하면 1010
	for (int r = 0;diff > 0;r++) { 
		if (diff & 1) {
			a = Parent[r][a];
		}
		diff >>= 1;
	}

	// Step 2 : LCA 찾기
	while (a != b) {
		int r;
		for (r = 0;r < 18;r++) {
			if (Parent[r][a] == Parent[r][b]) break;
		}
		if (r>0) --r;
		a = Parent[r][a], b = Parent[r][b];
	}
	return a;// a=b
}
