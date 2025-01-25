commands = list(input())

# Write your code here!

x,y = 0,0

dxs=[-1,0,1,0]
dys=[0,1,0,-1]
dir = 0

time = 0

for i in commands:
    if i == "R":
        dir = (dir+1)%4

    elif i=="L":
        dir = (dir+3)%4

    elif i=="F":
        x = x + dxs[dir]
        y = y + dys[dir]

    time += 1
    if x==0 and y==0:
        print(time)
        break
    if time==len(commands) and (x!=0 or y!=0):
        print(-1)
    