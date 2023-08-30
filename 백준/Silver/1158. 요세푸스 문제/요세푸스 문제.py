N,K = map(int, input().split())
lst = [i for i in range(1,N+1)]
idx = K-1
ans = []
while len(lst)>1:
    ans.append(lst[idx])
    lst.pop(idx)
    idx = (idx+K-1)%len(lst)
ans.append(lst[0])
print('<'+', '.join(map(str, ans))+'>')