n = int(input())
count = 1
result = 0

num = []

for _ in range(n):
    num.append(int(input()))


for i in range(n):
    if i==0 or num[i] == num[i-1]:
        count+=1
        if result < count:
            result = count
    elif num[i] != num[i-1]:
        count=1

print(result)