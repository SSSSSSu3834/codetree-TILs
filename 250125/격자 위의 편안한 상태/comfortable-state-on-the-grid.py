n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!

board = [[0 for _ in range(n)] for _ in range(n)]

dxs=[-1,1,0,0]
dys=[0,0,-1,1]

def in_range(x,y):
    return x>=0 and x <n and y>=0 and y<n

for x,y in points:
    x = x-1
    y=y-1
    cnt = 0
    if in_range(x,y):
        board[x][y] =1

        for i in range(4):
            nx= x+dxs[i]
            ny= y+dys[i]

            if in_range(nx,ny) and board[nx][ny] == 1:
                cnt +=1

    if cnt ==3:
        print(1)
    else:
        print(0)

