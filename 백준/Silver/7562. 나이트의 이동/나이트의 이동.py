from collections import deque

def bfs(start ,end):
    queue = deque([start])
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]]=1
    while queue:
        si,sj = queue.popleft()
        if (si,sj)==end:
            return visited[end[0]][end[1]]-1

        for (di,dj) in ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)):
            ni,nj = si+di, sj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                visited[ni][nj]=visited[si][sj]+1
                queue.append((ni,nj))




T = int(input())
for _ in range(T):
    N = int(input())
    board =[[0]*N for _ in range(N)]

    si,sj = map(int, input().split())
    ei,ej = map(int, input().split())
    print(bfs((si,sj),(ei,ej)))