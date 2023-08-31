N = int(input())
lst = []
for _ in range(N):
    lst.append(float(input()))

arr = [0 for _ in range(N)]
arr[0] = lst[0]

for i in range(1,N):
    arr[i] = max(arr[i-1]*lst[i], lst[i])
print(f'{max(arr):.3f}')
