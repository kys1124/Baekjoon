N =int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def make_line(si,sj,d1,d2):
    v = [[0]*N for _ in range(N)]
    v[si][sj]=5
    v[si+d2][sj+d2]=5
    v[si+d1][sj-d1]=5
    for mul in range(1,d1+1):
        v[si+mul][sj-mul] =5
        v[si+d2+mul][sj+d2-mul]=5
    for mul in range(1,d2+1):
        v[si+mul][sj+mul] = 5
        v[si+d1+mul][sj-d1+mul]=5
    return v

def make_group(si,sj,d1,d2,v):
    for i in range(si+d1):
        for j in range(sj+1):
            if v[i][j]==0:
                v[i][j]=1
            else:
                break

    for i in range(sj+1,N):
        for j in range(si+d2+1):
            if v[j][i]==0:
                v[j][i]=2
            else:
                break

    for i in range(si+d1,N):
        for j in range(sj-d1+d2):
            if v[i][j]==0:
                v[i][j]=3
            else:
                break

    for i in range(sj-d1+d2,N):
        for j in range(N-1,si+d2,-1):
            if v[j][i]==0:
                v[j][i]=4
            else:
                break
    return v

ans = 987654321
for si in range(1,N-1):
    for sj in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if not(si+d1+d2<=N-1 and 0<=sj-d1 and sj+d2<=N-1):
                    continue
                v = make_line(si,sj,d1,d2)
                v = make_group(si,sj,d1,d2,v)
                g1,g2,g3,g4,g5 =0,0,0,0,0

                for i in range(N):
                    for j in range(N):
                        if v[i][j]==1:
                            g1+=arr[i][j]
                        elif v[i][j]==2:
                            g2+=arr[i][j]
                        elif v[i][j]==3:
                            g3+=arr[i][j]
                        elif v[i][j]==4:
                            g4+=arr[i][j]
                        else:
                            g5+=arr[i][j]
                sm = max(g1,g2,g3,g4,g5)-min(g1,g2,g3,g4,g5)

                ans = min(ans, sm)
print(ans)