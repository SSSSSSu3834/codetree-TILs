n = int(input())

people = []

class Person:
    def __init__(self, tall, weight, num):
        self.tall = tall
        self.weight = weight
        self.num = num


for i in range(n):
    t, w = map(int, input().split())
    people.append(Person(t, w, i+1))

people.sort(key = lambda x: (-x.tall, -x.weight, -x.num))    

for i in people:
    print(i.tall, i.weight, i.num)