n = int(input())

num = list(map(int, input().split()))

for _ in range(n-1):
    for i in range(n-1):
        if num[i] > num[i+1]:
            num[i], num[i + 1] = num[i + 1], num[i]
 


for i in num:
    print(i, end=" ")