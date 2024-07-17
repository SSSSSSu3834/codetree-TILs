class Person:
    def __init__(self, name, add, place):
        self.name = name
        self.add = add
        self.place = place


people = []
n = int(input())

for _ in range(n):
    name, add, place = input().split()
    people.append(Person(name, add, place))


people.sort(key=lambda person: person.name)

print("name",people[n-1].name)
print("addr",people[n-1].add)
print("city",people[n-1].place)