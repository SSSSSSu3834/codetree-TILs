n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))

max = 0
result = 0
count = 0

for i in range(n):
    if num[i]> num[i-1] and num[i] > max:
        max = num[i]
        count+=1
        if result < count:
            result = count
    else:
        count = 1
        max = 0
        if result < count:
            result = count

print(result)