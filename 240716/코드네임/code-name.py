class Score:
    def __init__(self, code, score):
        self.code = code
        self.score = int(score)

scores = []

for _ in range(5):
    c, s = input().split()
    scores.append(Score(c, s))

minS = Score("", 100)

for i in range(5):
   if minS.score > int(scores[i].score):
    minS = scores[i]

print(minS.code, minS.score)