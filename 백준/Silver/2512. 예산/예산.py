N = int(input())
budget = list(map(int, input().split()))
M = int(input()) # 총예산

budget.sort()
left = 0
right = M

def cal(k,M):
    for x in budget:
        if x>k:
            M-=k
        else:
            M-=x
        if M<0:
            return False
    return True

ans = 0
if sum(budget)<=M:
    print(budget[-1])

else:
    while left<=right:
        mid = (left+right)//2 #상한액

        if cal(mid,M):
            ans = max(mid, ans)
            left = mid+1

        else:
            right = mid-1


    print(ans)
