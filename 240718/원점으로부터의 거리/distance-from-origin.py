n = int(input())

# 원점에서 짧은 거리부터 출력(오름차순 출력)
spots= []

for i in range(n):
    x, y = map(int, input().split())
    spots.append((x, y, i+1))

spots.sort(key = lambda x: (abs(0-x[0])+ abs(0-x[1]), x[2]))

for i in spots:
    print(i[2])