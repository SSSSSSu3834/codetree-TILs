n, m = map(int, input().split())

dir = 0

dxs=[1,0,-1,0]
dys=[0,1,0,-1]

cnt = 0
x=0
y=0

board = [[ 0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y >=0 and y<m 

board[0][0] = 1

for i in range(2, n*m+1):

    nx = x + dxs[dir]
    ny = y + dys[dir]


    if not in_range(nx, ny) or board[nx][ny] !=0:
        dir= (dir +1)%4

        nx = x + dxs[dir]
        ny = y + dys[dir]
    

    board[nx][ny] = i
    x = nx
    y = ny


for i in range(n):
    for j in range(m):
        print(board[i][j], end=" ")
    print()
