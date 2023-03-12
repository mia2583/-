N, M = map(int, input().split(" ")) # x범위는 N과 관련됨.
graph = []
check = [[0]*M for _ in range(N)]
for _ in range(N):
    i = list(map(int, input().split(" ")))
    graph.append(i)
count = 0
def dfs():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    stack = [(0,0)]
    graph[0][0] = 3
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if graph[nx][ny] == 0:
                    stack.append((nx,ny))
                    graph[nx][ny] = 3

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                count_3 = 0
                for k in range(4):
                    if nx>=0 and nx<N and ny>=0 and ny<M:
                        ni, nj = i+dx[k], j+dy[k]
                        if graph[ni][nj] == 3:
                            count_3 += 1
                if count_3 > 1:
                    graph[i][j] = 4

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 2:
                graph[i][j] = 0

for _ in range(1000):
    new_check = 0
    dfs()
    count += 1
    for k in graph:
        if 1 in k:
            new_check += 1
    if new_check == 0:
        break
    
print(count)
