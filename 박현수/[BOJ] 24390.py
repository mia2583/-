from collections import deque
visited = []
min, sec = map(int, input().split(":"))
a,b,c,s = 10, 60, 600, 30
graph = {s:[c,b,a], a:[a], b:[b,a], c:[c,b,a]}
total = min*60 + sec
if sec >= 30:
    root = s
elif total >= 600:
    root = c
elif total >= 60:
    root = b
else:
    root = a
count = 0
queue = deque([[root, total-root, 1]])
while queue:
    n = queue.popleft()
    if n[1] == 0 and n[2] == 1:
        count += 1
        break
    for i in graph[n[0]]:
        if n[1]-i < 0:
            continue
        queue.append([i, n[1]-i,n[2]+1])
        if (n[1]-i) == 0:
            count = n[2]+1
            break
        break
if root == s:
    print(count)
else:
    print(count + 1)
