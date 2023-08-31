import heapq

n = int(input())
arr=[]
answer =[]
for _ in range(n):
    x = int(input())
    if x!=0:
        heapq.heappush(arr, x)
    else:
        if len(arr)==0:
            answer.append(0)
        else:
            answer.append((heapq.heappop(arr)))
print(*answer)
