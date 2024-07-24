# N * N 격자를 벗어나지 않으면서, 3 * 3 크기 격자 내에 들어올 수 있는 최대 동전의 수를 출력해주세요.
n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))



def findMax(row_s, row_e, col_s, col_e):
    sumCoin = 0
    for i in range(row_s, row_e+1):
        for j in range(col_s, col_e+1):
            
            sumCoin += board[i][j]

    return sumCoin

sum = 0
maxCoin = 0

# 격자 탐색
for i in range(n):
    for j in range(n):
        if (j+2) >=n or (i+2) >=n :
            continue
        sum = findMax(i, i+2, j, j+2)

        maxCoin = max(maxCoin, sum)


print(maxCoin)