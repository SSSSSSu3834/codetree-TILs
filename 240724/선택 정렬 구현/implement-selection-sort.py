n = int(input())
num = list(map(int, input().split()))

for i in range(n - 1):
    min = i
    for j in range(i+1, n):
        if num[min]>num[j]:
            min = j
    
    num[i], num[min] = num[min], num[i]

for i in num:
    print(i, end=' ')