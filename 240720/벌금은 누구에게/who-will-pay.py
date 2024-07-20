n, m , k = map(int, input().split())
# 벌칙받은 애들 저장
target = []
count= 0

board = [[0] for _ in range(m)]


for i in range(m):
    target.append(int(input()))


for i in target:
    board[i-1][0] =  board[i-1][0] +1
    count +=1

    if board[i-1][0] >= k:
        print(i)
        break
    elif count == m:
        print(-1)