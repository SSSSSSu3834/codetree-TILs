n = int(input())

people = []

class Person:
    def __init__(self, name, tall, weight):
        self.name = name
        self.tall = tall
        self. weight = weight


for _ in range(n):

    data = input().split()
    
    n = data[0]
    t = int(data[1])
    w = int(data[2])
   

    people.append(Person(n,t,w))

people.sort(key = lambda x : x.tall)

for i in people:
    print(i.name, i.tall, i.weight)