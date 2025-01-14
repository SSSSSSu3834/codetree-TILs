dirs = input()

# Write your code here!
x,y = 0,0
dx, dy = [0,1,0,-1],[1,0,-1,0]

# 북쪽부터 시계 방향으로 dir 증가
dir = 0 

for i in list(dirs):
    if i=="R":
        dir=(dir + 1)% 4
    elif i == "L":
        dir = (dir + 3)% 4
    else:
        nx, ny = x + dx[dir], y + dy[dir]
        x=nx
        y=ny


print(x,y)
        
    






