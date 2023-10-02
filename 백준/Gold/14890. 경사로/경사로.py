N, L = map(int, input().split()) #N*N , L 경사로 길이
arr = [list(map(int, input().split())) for _ in range(N)]


vc = [[0]*N for _ in range(N)]
vr = [[0]*N for _ in range(N)]
ans = 0
for i in range(N):
    valr, valc = arr[0][i], arr[i][0]
    j = 1
    flagr, flagc = True, True
    while j <= N - 1:
        if arr[j][i] == valr:
            j += 1
            continue

        elif abs(arr[j][i] - valr) > 1:
            flagr = False
            break

        elif arr[j][i] - valr == 1:
            for idx in range(j-1, j-1-L, -1):
                if idx >= 0 and arr[idx][i] == valr and vr[idx][i] == 0:
                    continue
                else:
                    flagr = False
                    j = N
                    break
            else:
                for idx in range(j-1, j-1- L, -1):
                    vr[idx][i] = 1
                valr = arr[j][i]
                j += 1

        elif valr - arr[j][i] == 1:
            for idx in range(j, j + L):
                if idx < N and arr[idx][i] == valr - 1 and vr[idx][i] == 0:
                    continue
                else:
                    flagr = False
                    j = N
                    break
            else:
                for idx in range(j, j + L):
                    vr[idx][i] = 1
                valr = arr[j][i]
                j += L
    if flagr:
        ans += 1

    j = 1
    while j<=N-1:
        if arr[i][j]==valc:
            j+=1
            continue

        elif abs(arr[i][j]-valc)>1:
            flagc =False
            break

        elif arr[i][j]-valc==1:
            for idx in range(j-1, j-1-L,-1):
                if idx>=0 and arr[i][idx]==valc and vc[i][idx]==0:
                    continue
                else:
                    flagc =False
                    j=N
                    break
            else:
                for idx in range(j-1, j-1-L,-1):
                    vc[i][idx]=1
                valc = arr[i][j]
                j+=1

        elif valc-arr[i][j]== 1:
            for idx in range(j, j+L):
                if idx<N and arr[i][idx]==valc-1 and vc[i][idx]==0:
                    continue
                else:
                    flagc=False
                    j=N
                    break
            else:
                for idx in range(j, j+L):
                    vc[i][idx]=1
                valc = arr[i][j]
                j +=L
    if flagc:
        ans+=1

print(ans)
