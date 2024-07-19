# 키 작은 순(오름차), 몸무게 큰 순(내림차)
# 번호는 입력 순 대로

n = int(input())

result = []

for i in range(n):
    h, w = map(int,input().split())
    result.append((h, w, i+1))


result.sort(key = lambda x: (x[0], -x[1]))

for i in result:
    print(i[0], i[1], i[2])