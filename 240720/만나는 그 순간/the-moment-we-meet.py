n , m = map(int, input().split())

a = []
b=[]
lineA = []
lineB = []

for i in range(n):
    data = input().split()
    d= data[0]
    t = int(data[1])

    a.append((d, t))

for i in range(m):
    data = input().split()
    d= data[0]
    t = int(data[1])

    b.append((d, t))

x= 0
x2 = 0

for i in a:
    if i[0] == 'R':
        for j in range(i[1]):
            lineA.append(x2+1)
            x2 +=1
    if i[0] == 'L':
        for j in range(i[1]):
            lineA.append(x2-1)
            x2 -=1

for i in b:
    if i[0] == 'R':
        for j in range(i[1]):
            lineB.append(x+1)
            x +=1
    if i[0] == 'L':
        for j in range(i[1]):

            lineB.append(x-1)
            x-=1

for i in range(len(lineA)):
    if lineA[i] == lineB[i] and (i != 1):
        print(i+1)
        break
    if i == (len(lineA) -1) :
        
        print(-1)