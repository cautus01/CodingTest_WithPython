#include <iostream>
using namespace std;

int N, M, K;
long long tree[1024 * 1024 * 2];
int tmpN = 0;

void update(int a, long long b) {
    // a번째 값 > leftNode는 tmpN부터 시작한다.따라서
    a = a + tmpN - 1;
    tree[a] = b;
    while (a > 1) {
        a = a >> 1; // 2일 때 여기 들어와서 1이 된다.
        tree[a] = tree[a * 2] + tree[a * 2 + 1];
    }
}
long long get_sum(int a, int b) { // 1번째~3번째
    a = a + tmpN - 1;
    b = b + tmpN - 1;
    long long sum = 0;

    while (a <= b) { // a와 b가 엇갈리지 않는 경우에는 계속해서 연산
        // a가 right_child 라면 항상 홀수이다.
        if ((a & 1) == 1) sum += tree[a];
        // b가 left_child 라면
        if ((b & 1) == 0) sum += tree[b];
        // a는 더하든 말든 상관없이 항상 오른쪽 parent으로 올라간다.
        a = (a + 1) >> 1;
        // b는 더하든 말든 상관없이 항상 왼쪽 parent으로 올라간다.
        b = (b - 1) >> 1;
    }
    return sum;
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M >> K; // N,M,K 입력
    // 1. tree의 배열 크기 정하기 = tmpN *2
    // leftNode = N 1,000,000
    // tmpN = leafnode 개수

    for (tmpN = 1;tmpN < N;tmpN *= 2);

    // 2. tree 내 값 초기화
       // 2-1. 입력 leafnode
    for (int i = 0;i < N;i++) {
        cin >> tree[tmpN + i];
       }
    for (int i = tmpN + N;i < tmpN * 2;i++) tree[i] = 0;
       // 2-2. internal node 계산
    for (int i = tmpN - 1;i >= 1;i--) tree[i] = tree[2 * i] + tree[2 * i + 1];

    long long a, b, c;
    for (int q = 0;q < M + K;q++) {
        cin >> a >> b >> c;
        if (a == 1) {
            // 3. update
            update(b, c);
        }
        else {
            // 4. 구간합 구하기
            cout << get_sum(b, c) << "\n";
        }
    }
}
