n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Write your code here!

# n: 행, m: 열
# dir은 오른쪽, 아래, 왼쪽, 위 순서로 증가

x=0
y=0
dxs=[0, 1, 0, -1]
dys=[1, 0, -1, 0]

# dir 처음은 0 으로 초기화
dir = 0

arr[x][y] = 1

def range_in(x,y):
    return x>=0 and x<n and y >=0 and y<m

# 채우는 숫자 기준으로 for문 돌림
for i in range(2, n*m+1):

    nx = x+dxs[dir]
    ny = y+dys[dir]

    if not range_in(nx,ny) or arr[nx][ny] != 0:
        # 방향 바꿔
        dir = (dir+1)%4

    x = x + dxs[dir]
    y = y + dys[dir]

    arr[x][y] = i
        

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")

    print()
