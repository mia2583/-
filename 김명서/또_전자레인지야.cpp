// https://www.acmicpc.net/problem/24390
// 24390번 또 전자레인지야?
// 1시간 + 30분

#include <bits/stdc++.h>
using namespace std;

string inputTime;
int M, S;
int answer=0;
queue<pair<int,int>> timeQueue; // (남은 시간, 버튼 클릭 횟수)
set<int> visited;

vector<string> split(string before, string delimeter) {
    vector<string> result;
    result.push_back(before.substr(0, 2));
    result.push_back(before.substr(3, 2));

    return result;
}

void input() {
    cin >> inputTime;
    vector<string> splitTime = split(inputTime, ":");
    // 문자열로 입력받은 것을 숫자로 변환하여 저장
    M = stoi(splitTime[0]);
    S = stoi(splitTime[1]);
}

void solve() {
    // 시작 시간에 따라 다르게 큐에 넣어준다.
    if(M==0&&S==0) timeQueue.push({0, 0});
    else if(S>=30) timeQueue.push({M*60+S-30, 1});
    else timeQueue.push({M*60+S, 1});

    while(!timeQueue.empty()) {
        pair<int,int> time = timeQueue.front();

        // 같은 남은 시간이라면 앞선게 더 효율적이니 굳이 큐에 넣지 않는다.
        // 참고) https://nanyoungkim.tistory.com/73
        int beforeLen = visited.size();
        visited.insert(time.first);
        timeQueue.pop();
        if(beforeLen==visited.size()) continue;

        // 시간이 끝나면 종료
        if(time.first == 0) { answer=time.second; break; }
        
        // bfs로 하나씩 접근
        if(time.first>=600) timeQueue.push({time.first-600, time.second+1});
        if(time.first>=60) timeQueue.push({time.first-60, time.second+1});
        if(time.first>=30) timeQueue.push({time.first-30, time.second+1});
        if(time.first>=10) timeQueue.push({time.first-10, time.second+1});
    }
}

void output() {
    cout << answer << endl;
}

int main() {
    input();
    solve();
    output();
    return 0;
}
