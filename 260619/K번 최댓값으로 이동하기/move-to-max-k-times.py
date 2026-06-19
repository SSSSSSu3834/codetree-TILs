from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
# bfs의 리턴값은 마지막 위치
# k번 bfs 반복

dx=[-1,1,0,0]
dy=[0,0,-1,1]
round = 0

def bfs(a, b):
    que = deque()
    que.append((a,b))
    start = grid[a][b]
    max_val = 0
    rc = []
    visitied = [[False]*n for _ in range(n)]



    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and start>grid[nx][ny] and visitied[nx][ny] == False:
                visitied[nx][ny] = True
                que.append((nx,ny))
                if max_val < grid[nx][ny]:
                    rc.clear()
                    rc.append((nx,ny))
                    max_val = grid[nx][ny]

                elif max_val == grid[nx][ny]:
                    rc.append((nx, ny))

    if rc:

        rc.sort()

        na, nb = rc[0]
        global round
        round += 1

        if k>round:
            bfs(na, nb)

        else:
            print(na+1, nb+1)
    else:
        print(a+1, b+1)
        exit()
        

r-=1
c-=1

if n==1 and k==1:
    print(r+1,c+1)
    exit()

else: bfs(r,c)
