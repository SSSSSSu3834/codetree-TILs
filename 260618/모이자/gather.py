import sys
n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

INT_MAX = sys.maxsize
ans = INT_MAX

for i in range(n):
    res = 0
    for j in range(n):
        # 현재 모이는 집 i
        dis=abs(i-j)
        res += A[j] * dis

    
    ans = min(ans, res)


print(ans)