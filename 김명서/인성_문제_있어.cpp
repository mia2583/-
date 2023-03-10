// https://www.acmicpc.net/problem/19952
// 19952번 인성 문제 있어?
// 시간 초과

#include<bits/stdc++.h>

using namespace std;

int T, W, H, O, F;
int startX, startY, goalX, goalY;
int x, y, h, f;
int maze[101][101] ={0, };
bool visited[101][101] ={0, };
queue<tuple<int, int, int>> location; // {x, y, 남은 힘}
bool complete = false;

void input() {
    // 세로 가로 장애물수 힘
    cin >> H >> W >> O >> F;
    // 출발 목적지
    cin >> startX >> startY >> goalX >> goalY;
    // 장애물 좌표 입력받기
    for(int i=0; i<O; i++) {
        cin >> x >> y >> h;
        maze[x][y] = h;
    }
}

void solve() {
    location.push({startX, startY, F});
    visited[startX][startY] = 1;

    while(!location.empty()) {
        tuple<int, int, int> current = location.front();
        x = get<0>(current);
        y = get<1>(current);
        f = get<2>(current);

        // 목표에 도달한 경우 종료
        if(x==goalX && y==goalY) { complete=true; break; }

        // 이동 가능 범위이고 방문하지 않은 곳인 경우
        if(x+1<=H && !visited[x+1][y]) { // 아래
            // 이동할 체력이 있는지 확인
            if(maze[x][y] >= maze[x+1][y]) h=1;
            else h = maze[x+1][y] - maze[x][y];

            if(f-h>=0) {
                // 이동 가능한 경우
                location.push({x+1, y, f-1});
                visited[x+1][y] = 1;
            }
        }
        if(x-1>0 && !visited[x-1][y]) { // 위
            if(maze[x][y] >= maze[x-1][y]) h=1;
            else h = maze[x-1][y] - maze[x][y];

            if(f-h>=0) {
                location.push({x-1, y, f-1});
                visited[x-1][y] = 1;
            }
        }
        if(y+1<=W && !visited[x][y+1]) { // 오른쪽
            if(maze[x][y] >= maze[x][y+1]) h=1;
            else h = maze[x][y+1] - maze[x][y];

            if(f-h>=0) {
                location.push({x, y+1, f-1});
                visited[x][y+1] = 1;
            }
        }
        if(y-1>0 && !visited[x][y-1]) { // 왼쪽
            if(maze[x][y] >= maze[x][y-1]) h=1;
            else h = maze[x][y-1] - maze[x][y];

            if(f-h>=0) {
                location.push({x, y-1, f-1});
                visited[x][y-1] = 1;
            }
        }
        location.pop();
    }

}

void output() {
    if(complete) cout << "잘했어!!" << endl;
    else cout << "인성 문제 있어??" << endl;
}

int main() {
    cin >> T;
    while(T--) {
        // 
        fill(&maze[0][0], &maze[101][101], 0);
        fill(&visited[0][0], &visited[101][101], 0);
        location = queue<tuple<int, int, int>>();
        complete = false;
        input();
        solve();
        output();
    }
    return 0;
}
