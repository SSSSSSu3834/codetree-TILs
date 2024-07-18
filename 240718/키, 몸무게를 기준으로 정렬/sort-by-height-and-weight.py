n = int(input())

result = []

for _ in range(n):
    data = input().split()
    n = data[0]
    h = int(data[1])
    w = int(data[2])

    result.append((n, h, w))

# 키 기준 오름차순, 몸무게 기준 내림차순
result.sort(key = lambda x: (x[1], -x[2]))

for i in result:
    print(i[0], i[1], i[2])