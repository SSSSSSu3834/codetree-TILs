K, N = map(int, input().split())

# Please write your code here.
answer = []

def choose(n):
    if N == n:
        
        for e in answer:
            print(e, end=" ")
        print()
        return


    for i in range(K):
        answer.append(i+1)
        choose(n+1)
        answer.pop()

    return


choose(0)