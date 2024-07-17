class Weather:
    def __init__(self, date, day, weath):
        self.date= date
        self.day = day
        self.weath = weath


n = int(input())

inform = []

for _ in range(n):
    date, day,weath = input().split()
    inform.append(Weather(date, day,weath))

 
for i in inform:
    if i.weath == "Rain":
        print(i.date, i.day, i.weath)
        break