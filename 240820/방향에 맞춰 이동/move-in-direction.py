n = int(input())

result = []

for _ in range(n):
    
    data = input().split()
    d = data[0]
    m = int(data[1])

    result.append((d, m))


x, y = 0,0

for i in range(n):
    if result[i][0] == "W":
        for _ in range(result[i][1]):
            dy = y - 1
            y = dy

    if result[i][0] == "S":
        for _ in range(result[i][1]):
            dx = x -1
            x = dx

    if result[i][0] == "N":
        for _ in range(result[i][1]):
            dx = x +1
            x= dx

    if result[i][0] == "E":
        for _ in range(result[i][1]):
            dy = y + 1
            y = dy

print(y, x)