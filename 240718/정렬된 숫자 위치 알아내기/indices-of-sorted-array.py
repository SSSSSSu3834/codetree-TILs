n = int(input())

num = list(map(int, input().split()))

result = []

class Num:
    def __init__(self, num, sun, idx=0):
        self.num = num
        self.sun = sun
        self.idx = idx



for i in range(n):
    result.append(Num(num[i], i))

result.sort(key = lambda x: x.num)

for i in range(n):
    result[i].idx = i+1


result.sort(key = lambda x: x.sun)

for i in result:
    print(i.idx, end=" ")