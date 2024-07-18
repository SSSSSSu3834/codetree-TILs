# 이름순 정렬, 키 큰 순 정렬

people = []

for _ in range(5):
    data = input().split()
    n = data[0]
    t = int(data[1])
    w = float(data[2])

    people.append((n,t,w))

# 이름 순 정렬
people.sort(key = lambda x: x[0])

print("name")
for i in people:
    print(i[0], i[1], i[2])


# 키 순 정렬
people.sort(key = lambda x: -x[1])

print()
print("height")
for i in people:
    print(i[0], i[1], i[2])