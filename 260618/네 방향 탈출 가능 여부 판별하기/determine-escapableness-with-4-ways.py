from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [1,-1,0,0]
dy = [0,0,1,-1]

x,y = 0,0

que = deque()
que.append((x,y))

while que:
    x, y = que.popleft()

    if x == n-1 and y == m-1:
        print(1)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and a[nx][ny] == 1:
            que.append((nx,ny))
            a[nx][ny] = 0


print(0)