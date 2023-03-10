from collections import deque
T = int(input())
for i in range(T):
    H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split(" "))
    graph = [[0]*W for _ in range(H)]
    check = [[0]*W for _ in range(H)]
    force = [[-1]*W for _ in range(H)]
    for q in range(O):
        i, j, k = map(int, input().split(" "))
        graph[i-1][j-1] = k
    start, end = (Xs-1, Ys-1), (Xe-1, Ye-1)
    force[start[0]][start[1]] = F
    queue = deque([start])
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(new_x>=0 and new_x < H and new_y >= 0 and new_y < W):
                if(check[new_x][new_y] == 0):
                    if(force[x][y] >= graph[new_x][new_y]-graph[x][y]):
                        check[new_x][new_y] = 1
                        queue.append((new_x,new_y))
                        force[new_x][new_y] = force[x][y]-1
    if force[end[0]][end[1]] >= 0:
        print("잘했어!!")
    else:
        print("인성 문제있어??")
