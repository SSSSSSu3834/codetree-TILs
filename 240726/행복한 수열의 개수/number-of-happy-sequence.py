# 행복한 수열 = 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
n,m = map(int, input().split())
num = []

result = 0 

for _ in range(n):
    num.append(list(map(int, input().split())))


for i in range(n):
    count=1
    for j in range(n):
        # 열에대한 순열
        if j !=0 and num[i][j] == num[i][j-1]:
            count+=1
        else:
            count = 1
        if count >= m:
            result +=1
            break


# 행에다한 수열
for i in range(n):
    count=1
    for k in range(n):
        if k !=0 and num[k][i] == num[k-1][i]:
            count+=1
        else:
            count = 1
        if count >= m:
            result += 1
            break

    

    

print(result)