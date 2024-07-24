n = int(input())

num = list(map(int, input().split()))

for i in range(1, n):
    # j는 현재 index바로 전
    j = i-1
    key = num[i]
    while( j>=0 and num[j] > key):
        num[j+1] = num[j]
        j-=1
        num[j+1] = key

    
for i in num:
    print(i, end=" ")