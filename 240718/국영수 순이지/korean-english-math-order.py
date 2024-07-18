n = int(input())

scores = []

class Score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


for _ in range(n):
    data = input().split()
    n = data[0]
    k = int(data[1])
    e = int(data[2])
    m = int(data[3])

    scores.append(Score(n, k, e, m))

scores.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

for i in scores:
    print(i.name, i.kor, i.eng, i.math)