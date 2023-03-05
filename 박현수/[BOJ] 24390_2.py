from collections import deque
M, S = map(int, input().split(":"))
time = [600,60,10]
visited = []
total = M*60 + S
if S>=30:
    total -= 30
def bfs():
    if total==0:
        return 1
    queue = deque([[total,1]])
    while queue:
        n = queue.popleft()
        for i in time:
            if n[0]-i<0:
                continue
            elif n[0]-i==0:
                return n[1]+1
            else:
                if n[0]-i in visited:
                    continue
                else:
                    visited.append(n[0]-i)
                    queue.append([n[0]-i,n[1]+1])
print(bfs())
