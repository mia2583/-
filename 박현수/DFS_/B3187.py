R, C = map(int, input().split(" "))
graph = []
check = [[0]*C for _ in range(R)]
for _ in range(R):
    a = list(map(str, input()))
    graph.append(a)
res_v = 0
res_k = 0
def dfs(root):
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    v,k = 0,0
    stack = [root]
    while stack:
        x, y = stack.pop()
        if check[x][y]==0:
            if graph[x][y] == "v":
                v += 1
            elif graph[x][y] == "k":
                k += 1
            check[x][y] = 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx>=0 and nx<R and ny>=0 and ny<C:
                    if check[nx][ny] == 0:
                        stack += [(nx,ny)]
    if v>=k:
        k = 0
    else:
        v = 0
    return v,k

for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            check[i][j] = 1

for i in range(R):
    for j in range(C):
        if check[i][j] == 0:
            v, k = dfs((i,j))
            res_v += v
            res_k += k

print(res_k,res_v)
