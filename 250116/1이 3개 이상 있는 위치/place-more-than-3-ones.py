n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

cnt_one = 0
cnt_all = 0 

dxs, dys = [1,-1,0,0] , [0,0,1,-1]


def range_in (x,y):
    return x<n and x>=0 and y<n and y>=0

for x in range(n):
    for y in range(n):
        cnt_one = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if range_in(nx, ny) and grid[nx][ny] == 1:
                cnt_one = cnt_one +1
                

                if cnt_one == 3:
                    cnt_all = cnt_all + 1
                    cnt_one = 0
                    break
                    
                    
        
        
        
print(cnt_all)