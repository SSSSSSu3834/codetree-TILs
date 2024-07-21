n,m = map(int, input().split())

a=[]
b = []
lineA = []
lineB = []
total = 0
count = 0

ax = 0
bx = 0

for _ in range(n):
    data = input().split()
    t=int(data[0])
    d = data[1]
    a.append((t,d))

for _ in range(m):
    data = input().split()
    t=int(data[0])
    d = data[1]
    b.append((t,d))

for i in a:
    if i[1] == 'L':
        for j in range(i[0]):
            lineA.append(ax-1)
            ax -=1
    if i[1] == 'R':
        for j in range(i[0]):
            lineA.append(ax+1)
            ax +=1

for i in b:
    if i[1] == 'L':
        for j in range(i[0]):
            lineB.append(bx-1)
            bx -=1
    if i[1] == 'R':
        for j in range(i[0]):
            lineB.append(bx+1)
            bx +=1

# 두 리스트의 길이를 맞추기 위해 나머지 시간 동안 위치를 유지
max_length = max(len(lineA), len(lineB))
# 맨 끝요소를 두 리스트의 길이 차이만큼 추가해줌
lineA.extend([lineA[-1]] * (max_length - len(lineA)))
lineB.extend([lineB[-1]] * (max_length - len(lineB)))

# 두 로봇이 같은 위치에 있는 경우를 세기
count = 0
for i in range(1, max_length):
    if lineA[i] == lineB[i] and lineA[i-1] != lineB[i-1]:
        count += 1

print(count)