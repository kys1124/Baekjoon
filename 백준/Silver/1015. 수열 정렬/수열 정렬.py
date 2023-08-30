N = int(input())
A = list(map(int, input().split()))
idx = [i for i in range(N)]
A = list(zip(A,idx))
A = sorted(A, key=lambda x:x[0])
P =[0]*N

for idx, (_,j) in enumerate(A):
    P[j]=idx
print(*P)