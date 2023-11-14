N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1 석순, 2 아리시작, 3 보스시작, 0 아무것도 없음.

A, D, B, E = map(int, input().split())  # 아리 체력 공격력 보스 체력 공격력
dir = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def find():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 3: #보스이면
                bi, bj = i, j
                for d in range(4): #인접한 곳 탐색해서 아리 위치 찾기.
                    ni, nj = bi + dir[d][0], bj + dir[d][1]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 2:
                        return ni, nj, bi, bj, d


ai, aj, bi, bj, sd = find()  # 아리 위치, 보스위치, 처음 방향
ad, bd = sd, sd

def ari_attack(D, B):  # 아리 공격
    return B - D

def move_ari(ai, aj, ad):
    global A
    ni, nj = ai + dir[ad][0], aj + dir[ad][1]
    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
        arr[ai][aj] = 0
        arr[ni][nj] = 2
        return ni, nj, ad
    else:
        for _ in range(3):
            ad = (ad + 1) % 4
            A -= 1
            ni, nj = ai + dir[ad][0], aj + dir[ad][1]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                arr[ai][aj] = 0
                arr[ni][nj] = 2
                return ni, nj, ad
        else:
            A-=1
            return ai, aj, (ad+1)%4


def find_suksoon(bi, bj, bd):
    cnt = 1
    for mul in range(1, M * N + 1):
        for _ in range(mul):
            ni, nj = bi + dir[bd][0], bj + dir[bd][1]
            if 0 <= ni < N and 0 <= nj < M:
                cnt += 1
                if arr[ni][nj] == 1:
                    return ni, nj
                elif cnt == N * M:
                    return -1, -1
            bi, bj = ni, nj

        bd = (bd + 1) % 4
        for _ in range(mul):
            ni, nj = bi + dir[bd][0], bj + dir[bd][1]
            if 0 <= ni < N and 0 <= nj < M:
                cnt += 1
                if arr[ni][nj] == 1:
                    return ni, nj
                elif cnt == N * M:
                    return -1, -1
            bi, bj = ni, nj
        bd = (bd + 1) % 4


def bfs(ai, aj, bi, bj, E):
    q = [(bi, bj)]
    v = [[0] * M for _ in range(N)]
    v[bi][bj] = 1
    cnt = 0
    while q:
        temp_q = []
        for i in range(len(q)):
            ci, cj = q[i]
            if (ci, cj) == (ai, aj):
                return E - cnt
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and (arr[ni][nj] != 1 and arr[ni][nj]!=3):
                    temp_q.append((ni, nj))
                    v[ni][nj] = 1
        cnt += 1
        if cnt >= E:
            return 0
        q = temp_q
    return 0


ans = ''
while True:
    B = ari_attack(D, B)
    if B <= 0:
        ans = "VICTORY!"
        break
    nai, naj, nad = move_ari(ai, aj, ad)
    if A <= 0:
        ans = "CAVELIFE..."
        break

    si, sj = find_suksoon(bi, bj, bd)
    if (si, sj) != (-1, -1):
        A -= bfs(nai, naj, si, sj, E)
        if A <= 0:
            ans = "CAVELIFE..."
            break

    if arr[ai][aj] != 2:
        arr[bi][bj] = 0
        bi, bj, bd = ai, aj, nad
        arr[bi][bj] = 3

    ai, aj, ad = nai, naj, nad

print(ans)