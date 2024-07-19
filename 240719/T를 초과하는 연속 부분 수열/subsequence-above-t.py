n, t = map(int, input().split())

count = 0
result = 0

num = list(map(int,input().split()))


for i in range(n):
    if i==0 and (num[i] > t):
        count = 1
        if count > result:
            result = count


    elif (num[i] > t) and (num[i] > num[i-1]):

        count +=1
        if count > result:
            result = count
    else:
        count = 0
        if count > result:
            result = count
        

print(result)