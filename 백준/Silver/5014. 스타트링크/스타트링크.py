F,S,G,U,D = map(int, input().split()) # F: 건물 층 개수, G 스타트링크 위치(목적), S 현재 위치,
# U 위로 U층, D 아래로 D층
# 이동 불가능 층수면 작동 x #건물은 1~F층
from collections import deque


def bfs():
    v = [float('inf')]*(F+1)
    q = deque([(S, 0)])
    v[S] = 0

    while q:
        c, cnt = q.popleft()

        if c+U<=F and v[c+U]>cnt+1:
            v[c+U]=cnt+1
            q.append((c+U,v[c+U]))

        if c-D>=1 and v[c-D]>cnt+1:
            v[c-D]=cnt+1
            q.append((c-D, v[c-D]))

    return v[G]

ans = bfs()
if ans==float('inf'):
    print('use the stairs')
else:
    print(ans)