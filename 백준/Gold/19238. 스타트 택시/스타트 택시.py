N, M, E = map(int, input().split())
arr =[list(map(int, input().split())) for _ in range(N)]
si,sj = map(lambda x:int(x)-1, input().split())
people = {}
for _ in range(M):
    ci,cj, ei,ej = map(lambda x:int(x)-1, input().split())
    people[(ci,cj)] = (ei,ej)

def find_people(si,sj):
    q = [(si,sj)]
    v = [[0]*N for _ in range(N)]
    v[si][sj]=1
    cnt = 0
    if people.get((si,sj)):
        return cnt, si,sj
    while q:
        temp_q = []
        f_lst = []
        for i in range(len(q)):
            ci,cj = q[i]
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==0:
                    v[ni][nj] = 1
                    temp_q.append((ni,nj))
                    if people.get((ni,nj)):
                        f_lst.append((ni,nj))

        cnt+=1
        q =temp_q
        if f_lst:
            f_lst.sort()
            return cnt, f_lst[0][0], f_lst[0][1]
    return -1,-1,-1

def go(si,sj,ei,ej):
    v =  [[0]*N for _ in range(N)]
    q = [(si,sj)]
    v[si][sj]=1
    cnt = 0
    while q:
        temp_q =[]
        for i in range(len(q)):
            ci,cj = q[i]
            if (ci,cj)==(ei,ej):
                return cnt

            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj =ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]==0:
                    v[ni][nj]=1
                    temp_q.append((ni,nj))
        cnt+=1
        q = temp_q
    return -1


while people:
    cnt, si,sj = find_people(si,sj)
    if cnt==-1: #승객에게 가는 길이 막힘.
        E=-1
        break

    if E<cnt:
        E = -1
        break
    E-= cnt
    ei,ej = people[(si,sj)]
    cnt = go(si,sj,ei,ej)
    if cnt==-1: #승객을 목적지 까지 데려다 주는 것이 불가능.
        E = -1
        break

    if E-cnt<0: # 목적지까지 이동은 가능하나 연료 부족.
        E = -1
        break
    # 승객 도착.
    E+=cnt
    del people[(si,sj)] #승객 사전에서 삭제.
    si,sj = ei,ej

print(E)