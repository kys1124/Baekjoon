N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
ans = N
dic = {1:(2,3),2:(1,3),3:(1,2)}
def change(idx, num):
    cnt = 1
    mn = idx
    mx = idx
    for i in range(idx-1, max(-1,idx-4), -1):
        if lst[i]==num:
            cnt+=1
            mn = i
        else:
            break
    for i in range(idx+1, min(N,idx+4)):
        if lst[i]==num:
            cnt+=1
            mx=i
        else:
            break

    if cnt>=4:
        return 1,mn,mx
    else:
        return 0,mn,mx

def pang(lst):
    while len(lst)>=4:
        num = lst[0]
        cnt = 1
        idx = 0
        for i in range(1, len(lst)):
            if lst[i]==num:
                cnt+=1
            else:
                num = lst[i]
                cnt = 1
                idx = i

            if cnt>=4:
                end = i
                for j in range(i+1,len(lst)):
                    if num==lst[j]:
                        end = j
                    else:
                        break
                lst = lst[:idx]+lst[min(end+1,len(lst)):]
                break
        else:
            return lst
    return lst

for i in range(N):
    for num in dic[lst[i]]:
        flag, mn,mx = change(i,num)
        if flag==1:
            new = lst[:max(mn,0)]+lst[min(mx+1,N):]
            ans = min(ans, len(pang(new)))

print(ans)