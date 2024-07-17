class Test:
    def __init__(self, name="codetree", code = 50):
        self.name = name
        self.code = code

test1= Test()

n, c =input().split()
test2 = Test(n,c)

print("product",test1.code, "is", test1.name)
print("product",test2.code, "is", test2.name)