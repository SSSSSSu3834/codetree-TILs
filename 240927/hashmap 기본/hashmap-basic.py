n = int(input())

d= dict()

result = []

for i in range(n):
    result.append(list(input().split()))

print(result)

for i in result:
    if(i[0] == 'add'):
        d[i[1]] = i[2]
    elif(i[0] == "remove"):
        d.pop(i[1])
    elif(i[0] == "find"):
        if( i[1] in d):
            print(d[i[1]])
        else: print("None")