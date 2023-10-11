import heapq
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def prim():
    S = set()
    ans = 0
    pq = [(0,0)]
    while pq:
        cost, cur = heapq.heappop(pq)
        if cur in S:
            continue

        S.add(cur)
        ans += cost
        if len(S)==N:
            return ans


        for i in range(N):
            if i!=cur and i not in S:
                heapq.heappush(pq, (arr[cur][i], i))

print(prim())