N,M = map(int, input().split())

lst = [i for i in range(1,1+N)]

def reverse(i,j, lst):
    ans = []
    for x in range(j-1,i-2,-1):
        ans.append(lst[x])
    return ans



for _ in range(M):
    i,j = map(int ,input().split())

    ans = reverse(i,j, lst)
    lst[i-1:j] = ans

print(*lst)