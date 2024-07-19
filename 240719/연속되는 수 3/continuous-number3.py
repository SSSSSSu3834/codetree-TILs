n = int(input())
count = 1
result = 0

num = []

for _ in range(n):
    num.append(int(input()))


for i in range(n):
    
    if (num[i]<0 and num[i-1]<0) or (num[i]>0 and num[i-1]>0):
        count+=1
        if result < count:
            result = count
    # 만약 배열이 1개 라면 count값이 곧 result
    else:
        count = 1
        if result <= count:
            result = count
    

print(result)