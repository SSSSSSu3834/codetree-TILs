from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0

def bfs(a, b):
    cnt = 1
    if grid[a][b] == 0:
        grid[a][b] = 1
        cnt = 1
    else:
        return 0


    que = deque()
    que.append((a,b))


    

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and grid[nx][ny] == 0:
                que.append((nx,ny))
                grid[nx][ny] =1 
                cnt+= 1


    return cnt

for i in range(k):
    a, b = points[i]
    a= a-1
    b=b-1

    ans += bfs(a,b)


print(ans)