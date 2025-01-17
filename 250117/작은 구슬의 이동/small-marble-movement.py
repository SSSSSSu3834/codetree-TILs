n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Write your code here!

r= r-1
c = c-1

dic={
    "U": 0,
    "D": 3,
    "R": 1,
    "L": 2
}


dxs = [-1,0,0,1]
dys = [0,1,-1,0]

# 범위 유효성 검증
def range_in(x,y):
    return x>=0 and x<n and y>=0 and y<n

# dict 형태 사용해서 dir을 숫자로 다시 정의
dir = dic[d]

for t in range(t):
    nx = r + dxs[dir]
    ny = c + dys[dir]

    if range_in(nx, ny):
        r = nx
        c = ny
    else:
        dir = 3-dir

print(r+1, c+1)

