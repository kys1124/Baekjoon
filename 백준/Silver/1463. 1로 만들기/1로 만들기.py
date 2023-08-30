N = int(input())
cnt = [0]*(N+1)
for i in range(2,N+1):
    if i%2==0 and i%3==0:
        cnt[i] = min(cnt[i-1],cnt[i//2], cnt[i//3])+1
    elif i%2==0 and i%3!=0:
        cnt[i] = min(cnt[i-1], cnt[i//2])+1
    elif i%2!=0 and i%3==0:
        cnt[i] = min(cnt[i-1], cnt[i//3])+1
    else:
        cnt[i] = cnt[i-1]+1
print(cnt[N])
