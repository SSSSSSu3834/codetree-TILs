n = int(input())
count = 1
result = 0

num = []

for _ in range(n):
    num.append(int(input()))


for i in range(n):
    
    # 만약 배열이 1개 라면 count값이 곧 result
    if i == 0:
        count = 1
        if result <= count:
            result = count
    
    # 부호 같을 때 count올리고 result에 저장
    elif (num[i]<0 and num[i-1]<0) or (num[i]>0 and num[i-1]>0):
        count+=1
        if result < count:
            result = count

    # 부호 다를 때 count값 초기화함
    else:
        count = 1

    

print(result)