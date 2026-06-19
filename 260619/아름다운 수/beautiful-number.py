n = int(input())
ans = []
cnt=0

# Please write your code here.

def findAns(arr):
    pre = arr[0]
    round = 1
    global cnt
    for i in range(1,n):
        if  pre != arr[i]:
            if round % pre !=0:
                return
            elif round % pre == 0:
                round = 1
                pre= arr[i]
        else:   
            round += 1

    if round % pre ==0:
        # print(pre, round, arr[i])
        # print(arr)
        cnt+=1
    else:
        return


def backtracking(k):
    if n == k:
        findAns(ans)
        return


    for i in range(4):
        ans.append(i+1)
        backtracking(k+1)
        ans.pop()

    
    return


backtracking(0)
print(cnt)