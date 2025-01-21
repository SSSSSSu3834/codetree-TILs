N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Write your code here!

dxs=[0,1,0,-1]
dys=[1,0,-1,0]

x,y = 0,0

direct = {
    "N":0,
    "E":1,
    "S":2,
    "W":3
}

cnt = 0
bol = False

for i in range(N):
    for j in range(dist[i]):
        dirn = direct[dir[i]]
        x = x + dxs[dirn]
        y = y + dys[dirn]

        cnt+=1

        if x ==0 and y ==0 and bol == False:
            print(cnt)
            bol = True
            break


if not bol:
    print(-1)





