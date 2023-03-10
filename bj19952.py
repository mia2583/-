from collections import deque

H = 0
W = 0
maze = [[0] * 100 for row in range(100)]
visited = [[0] * 100 for row in range(100)]
hp = [[-1] * 100 for row in range(100)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def canJump(x, y, nx, ny):
    if hp[x][y] <= 0 or nx < 0 or nx >= H or ny < 0 or ny >= W or visited[nx][ny]:
        return 0

    diff = maze[nx][ny] - maze[x][y]
    if diff <= hp[x][y]:
        return 1

    return 0


T = int(input())

for t in range(T):
    H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split())

    maze = [[0] * W for row in range(H)]
    visited = [[0] * W for row in range(H)]
    hp = [[-1] * W for row in range(H)]

    for j in range(O):
        Xo, Yo, L = map(int, input().split())
        maze[Xo - 1][Yo - 1] = L

    queue = deque([(Xs - 1, Ys - 1)])
    hp[Xs - 1][Ys - 1] = F

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if canJump(x, y, nx, ny):
                hp[nx][ny] = hp[x][y] - 1
                queue.append((nx, ny))
                visited[nx][ny] = True

    if hp[Xe - 1][Ye - 1] < 0:
        print("인성 문제있어??")
    else:
        print("잘했어!!")






