import heapq

M, N = map(int, input().split())
k = int(input())
dic = {}
for _ in range(k):
    b, x1,y1, x2,y2 = map(int, input().split())
    dic[b] = (min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2))
sx,sy,ex,ey = map(int, input().split())

pq = []
v = [0]*(b+1)
def check(bus_num, dx,dy):
    x1,y1,x2,y2 = dic[bus_num]
    if (x1<=dx<=x2) and (y1<=dy<=y2):
        return True
    return False

def check2(cur, nxt):
    cx1, cy1, cx2, cy2 = dic[cur]
    nx1, ny1, nx2, ny2 = dic[nxt]
    if (cx1==cx2): #현재 내가 탄 버스가 세로로 운행 중.
        if (nx1<=cx1<=nx2) and ((cy1<=ny1<=cy2) or (cy1<=ny2<=cy2)): #가로로 겹치는 곳이 있어야 하고.
            return True
    else: #가로로 운행 중. cy1==cy2
        if (ny1<=cy1<=ny2) and ((cx1<=nx1<=cx2) or (cx1<=nx2<=cx2)):
            return True
    return False

for i in range(1,k+1):
    x1,y1,x2,y2 = dic[i]
    if (x1<=sx<=x2) and (y1<=sy<=y2):
        pq.append((1,i))

def solve():
    heapq.heapify(pq)
    while pq:
        cur_cnt, cur_bus = heapq.heappop(pq)
        if v[cur_bus]==1:
            continue
        v[cur_bus]=1

        if check(cur_bus, ex,ey):
            return cur_cnt

        for nxt in range(1,k+1):
            if v[nxt]==0 and check2(cur_bus,nxt):
                heapq.heappush(pq, (cur_cnt+1, nxt))

print(solve())