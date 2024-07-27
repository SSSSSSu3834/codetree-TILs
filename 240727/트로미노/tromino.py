# 트로미노(Tromino)는 폴리오미노(Polyomino) 중 하나로, 
# 세 개의 정사각형이 서로 인접하게 연결된 도형입니다. 

n,m = map(int,input().split())
num = []

for _ in range(n):
    num.append(list(map(int, input().split())))

maxValue = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    for j in range(m):
        C_sum = num[i][j]
        values = []

        for k in range(4):
            nx = i + dx[k] # 상하
            ny = j + dy[k] # 좌우

            if 0 <= nx < n and 0 <= ny < m:
                values.append(num[nx][ny])


        if len(values) == 4:
            for a in range(4):
                for b in range(a + 1, 4):
                    temp_sum = C_sum + sum(values) - values[a] - values[b]
                    maxValue = max(maxValue, temp_sum)
        elif len(values) == 3:
            for h in range(3):
                
                temp_sum = C_sum + sum(values) - values[h]
                maxValue = max(maxValue, temp_sum)

           


print(maxValue)