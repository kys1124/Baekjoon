N =int(input()) # 동기 수
M = int(input()) # 리스트 길이
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs():
    v = [0]*(N+1)
    v[1] = 1
    q = [1]
    cnt = 0
    while q:
        temp_q = []
        for i in range(len(q)):
            cur = q[i]
            for nxt in adj[cur]:
                if v[nxt]==0:
                    v[nxt]=1
                    temp_q.append(nxt)
        cnt+=1
        if cnt>=2:
            return sum(v)-1
        q = temp_q
    return sum(v)-1
print(bfs())