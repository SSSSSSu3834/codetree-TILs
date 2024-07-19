n, t = map(int, input().split())

count = 0
result = 0

num = list(map(int,input().split()))

print(num)


for i in range(n):
    if (num[i] > t) and (num[i] > num[i-1]):
        count +=1
        if count > result:
            result = count
    else:
        count = 0
        if count > result:
            result = count
        

print(result)