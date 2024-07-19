n, t = map(int, input().split())

count = 1
result = 0

num = list(map(int,input().split()))


for i in range(n):
    if (num[i] > t) and i == 0:
        count = 1
        if count > result:
            result = count


    elif (num[i] > t):
        if (num[i] > num[i-1]):
            count += 1
            if count > result:
                result = count

        if (num[i] < num[i-1]) and ((num[i] < num[i+1])):
            count = 1


        
    else:
        count = 0

if result < 2:
    print(0)
else:
    print(result)