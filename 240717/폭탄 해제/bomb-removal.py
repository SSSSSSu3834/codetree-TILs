class Code:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = input().split()
code1= Code(code, color, second)

print("code :", code1.code)
print("color :", code1.color)
print("second :", code1.second)