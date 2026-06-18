n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans = 0
for i in range(n):
    for j in range(n):
        res = 0
        if j+2 < n:
            for k in range(3):
                res += grid[i][j+k]
            
            ans = max(res, ans)

    if ans == 3:
        break


print(ans)

