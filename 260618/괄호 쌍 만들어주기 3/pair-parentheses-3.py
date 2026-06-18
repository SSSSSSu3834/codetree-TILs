A = input()

# Please write your code here.

n= len(A)
cnt =0
for i in range(n):
    if A[i] == ")":
        continue
    for j in range(i, n):
        if A[j] == ")":
            cnt += 1
        

print(cnt)