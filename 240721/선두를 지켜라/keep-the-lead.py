n, m = map(int, input().split())

a= []
b=[]
La = []
Lb = []
result = []
count = 0

for _ in range(n):
    v, t = map(int, input().split())
    a.append((v,t))
for _ in range(m):
    v, t = map(int, input().split())
    b.append((v,t))

totalTime = 0

for i in a:
    totalTime += i[1]

# a, b 초기값
ax = 0
bx = 0

for i in a:
    for j in range(i[1]):
        ax = ax + i[0]
        La.append(ax)

for i in b:
    for j in range(i[1]):
        bx = bx + i[0]
        Lb.append(bx)


for i in range(len(La)):

    if La[i] == Lb[i]:
          if La[i-1] > Lb[i-1]:
            result.append("A")
          else:
            result.append("B")
          

    if La[i] > Lb[i]:
        result.append("A")
    else:
        result.append("B")

for i in range(len(result)):
    if i==0:
        count = 0
    elif result[i] != result[i-1]:
        count+=1
    

print(count)